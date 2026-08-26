from models.vehicle import Car, Bike, Van
from models.customer import Customer
from models.admin import Admin
from services.vehicle_inventory import VehicleInventory
from services.rental_service import RentalService
from payments.card_payment import CardPaymentProcessor
from payments.upi_payment import UpiPaymentProcessor
from exceptions.rental_exceptions import RentalException
from datetime import date
from services.notification_service import NotificationService


def prompt_int(prompt_text, min_value=None):
    while True:
        raw = input(prompt_text).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if min_value is not None and value < min_value:
            print(f"Please enter a number >= {min_value}.")
            continue
        return value


def prompt_nonempty(prompt_text):
    while True:
        value = input(prompt_text).strip()
        if value:
            return value
        print("This can't be empty.")


def choose_payment_method(customer_name):
    print("Payment method: 1. Card  2. UPI")
    choice = prompt_int("Choose 1 or 2: ", min_value=1)
    if choice == 1:
        card_number = prompt_nonempty("Card number: ")
        return CardPaymentProcessor(card_number, customer_name)
    upi_id = prompt_nonempty("UPI ID (e.g. name@bank): ")
    return UpiPaymentProcessor(upi_id)


def build_seed_inventory(admin, inventory):
    admin.add_vehicle(inventory, Car("V101", "KA01AB1234", "Toyota", "Innova", 2000))
    admin.add_vehicle(inventory, Bike("V102", "KA01CD5678", "Yamaha", "FZ", 700))
    admin.add_vehicle(inventory, Van("V103", "KA01EF9012", "Tata", "Ace", 3000))


def print_menu():
    print("""
--- Vehicle Rental Management System ---
1. View available vehicles
2. Search vehicles
3. Register a customer
4. Rent a vehicle
5. Return a vehicle
6. Cancel a rental
7. View a customer's rental history
8. Admin: add a vehicle
9. Admin: set maintenance status
10. Admin: view all rentals
11. Exit
""")


def main():
    inventory = VehicleInventory()
    service = RentalService(inventory, NotificationService())
    admin = Admin("A001", "Priya Nair")
    customers = {}

    build_seed_inventory(admin, inventory)

    while True:
        print_menu()
        choice = prompt_int("Choose an option: ", min_value=1)

        try:
            if choice == 1:
                inventory.display_available()

            elif choice == 2:
                type_input = input("Vehicle type (Car/Bike/Van, blank for any): ").strip()
                price_input = input("Max daily price (blank for any): ").strip()
                vehicle_type = type_input or None
                max_price = float(price_input) if price_input else None
                results = inventory.search_vehicles(vehicle_type=vehicle_type, max_price=max_price)
                if not results:
                    print("No matching vehicles.")
                for vehicle in results:
                    vehicle.display_details()

            elif choice == 3:
                customer_id = prompt_nonempty("Customer ID: ")
                name = prompt_nonempty("Name: ")
                email = prompt_nonempty("Email: ")
                licence = prompt_nonempty("Driving licence number: ")
                customer = Customer(customer_id, name, email, licence)
                customers[customer_id] = customer
                print(f"Registered {name} as customer {customer_id}.")

            elif choice == 4:
                customer_id = prompt_nonempty("Customer ID: ")
                customer = customers.get(customer_id)
                if not customer:
                    print("No such customer. Register them first (option 3).")
                    continue
                vehicle_id = prompt_nonempty("Vehicle ID to rent: ")
                vehicle = inventory.get_vehicle(vehicle_id)
                if not vehicle:
                    print("No such vehicle.")
                    continue
                days = prompt_int("Rental duration (days): ", min_value=1)
                payment_processor = choose_payment_method(customer.name)
                rental = service.rent_vehicle(customer, vehicle, days, payment_processor)
                print(f"Rental confirmed: {rental.rental_id}")

            elif choice == 5:
                rental_id = prompt_nonempty("Rental ID to return: ")
                rental = service.get_rental(rental_id)
                if not rental:
                    print("No such rental.")
                    continue
                print(f"This rental was due back on: {rental.due_date}")
                date_input = input("Return date as YYYY-MM-DD (blank = today/on-time): ").strip()
                if date_input:
                    try:
                        year, month, day = map(int, date_input.split("-"))
                        return_date = date(year, month, day)
                    except ValueError:
                        print("Invalid date format, using today's date instead.")
                        return_date = date.today()
                else:
                    return_date = date.today()
                invoice = service.return_vehicle(rental, return_date=return_date)
                invoice.display()

            elif choice == 6:
                rental_id = prompt_nonempty("Rental ID to cancel: ")
                rental = service.get_rental(rental_id)
                if not rental:
                    print("No such rental.")
                    continue
                service.cancel_rental(rental)

            elif choice == 7:
                customer_id = prompt_nonempty("Customer ID: ")
                customer = customers.get(customer_id)
                if not customer:
                    print("No such customer.")
                    continue
                customer.display_rental_history()

            elif choice == 8:
                vehicle_id = prompt_nonempty("New vehicle ID: ")
                reg_number = prompt_nonempty("Registration number: ")
                brand = prompt_nonempty("Brand: ")
                model = prompt_nonempty("Model: ")
                rate = prompt_int("Daily rate: ", min_value=1)
                print("Type: 1. Car  2. Bike  3. Van")
                type_choice = prompt_int("Choose 1-3: ", min_value=1)
                vehicle_class = {1: Car, 2: Bike, 3: Van}.get(type_choice, Car)
                vehicle = vehicle_class(vehicle_id, reg_number, brand, model, rate)
                admin.add_vehicle(inventory, vehicle)

            elif choice == 9:
                vehicle_id = prompt_nonempty("Vehicle ID: ")
                vehicle = inventory.get_vehicle(vehicle_id)
                if not vehicle:
                    print("No such vehicle.")
                    continue
                flag_input = input("Under maintenance? (y/n): ").strip().lower()
                admin.set_vehicle_maintenance(vehicle, flag_input == "y")

            elif choice == 10:
                admin.view_all_rentals(service)

            elif choice == 11:
                print("Goodbye.")
                break

            else:
                print("Not a valid option.")

        except RentalException as error:
            print(f"Operation failed: {error}")
        except ValueError as error:
            print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()