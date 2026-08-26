from datetime import date, timedelta
from services.notification_service import NotificationService
from models.vehicle import Car, Bike, Van
from models.customer import Customer
from models.admin import Admin
from services.vehicle_inventory import VehicleInventory
from services.rental_service import RentalService
from payments.card_payment import CardPaymentProcessor
from payments.upi_payment import UpiPaymentProcessor
from persistence.data_store import save_inventory, save_customers
from exceptions.rental_exceptions import RentalException


def section(title):
    print(f"\n=== {title} ===")


def main():
    inventory = VehicleInventory()
    service = RentalService(inventory, NotificationService())
    admin = Admin("A001", "Priya Nair")

    # 1. Add one car, one bike, one van
    section("Setting up inventory")
    car = Car("V101", "KA01AB1234", "Toyota", "Innova", 2000)
    bike = Bike("V102", "KA01CD5678", "Yamaha", "FZ", 700)
    van = Van("V103", "KA01EF9012", "Tata", "Ace", 3000)
    admin.add_vehicle(inventory, car)
    admin.add_vehicle(inventory, bike)
    admin.add_vehicle(inventory, van)

    # Bonus: a fourth vehicle flagged under maintenance
    scooter = Bike("V104", "KA01GH3456", "Honda", "Activa", 500)
    admin.add_vehicle(inventory, scooter)
    admin.set_vehicle_maintenance(scooter, True)

    # 2. Register two customers
    customer_a = Customer("C001", "Ananya Sharma", "ananya@example.com", "DL-12345")
    customer_b = Customer("C002", "Rohan Verma", "rohan@example.com", "DL-67890")

    # 3. Display all available vehicles
    section("Available vehicles")
    inventory.display_available()

    # 4. Customer A rents the car for 3 days
    section("Customer A rents the car")
    print(f"Customer: {customer_a.name}")
    print(f"Selected vehicle: {car.vehicle_id}")
    print("Rental duration: 3 days")

    rental_date = date.today()
    card = CardPaymentProcessor("4111 1111 1111 1234", customer_a.name)
    try:
        rental = service.rent_vehicle(customer_a, car, 3, card, rental_date=rental_date)
    except RentalException as error:
        print(f"Rental failed: {error}")
        return

    # 5 & 6. Attempt to rent the same car to Customer B -> unavailable
    section("Customer B attempts to rent the same car")
    upi = UpiPaymentProcessor("rohan@upi")
    try:
        service.rent_vehicle(customer_b, car, 2, upi)
    except RentalException as error:
        print(f"Vehicle unavailable: {error}")

    # Bonus: Customer B tries a vehicle under maintenance
    section("Customer B attempts to rent a vehicle under maintenance")
    try:
        service.rent_vehicle(customer_b, scooter, 2, upi)
    except RentalException as error:
        print(f"Rental blocked: {error}")

    # Bonus: Customer B rents the van, then cancels it
    section("Customer B rents the van, then cancels")
    try:
        van_rental = service.rent_vehicle(customer_b, van, 2, upi)
        service.cancel_rental(van_rental)
    except RentalException as error:
        print(f"Rental failed: {error}")

    # 8. Return the car one day late
    section("Customer A returns the car (one day late)")
    return_date = rental_date + timedelta(days=4)
    invoice = service.return_vehicle(rental, return_date=return_date)

    # 9 & 10. Display the final invoice
    invoice.display()

    # 11. Confirm the returned car is available again
    print(f"\nVehicle returned successfully. {car.vehicle_id} available? {car.available}")

    # 12. Customer A's rental history
    section("Customer A's rental history")
    customer_a.display_rental_history()

    # Bonus: admin view of all rentals
    section("Admin view of all rentals")
    admin.view_all_rentals(service)

    # Bonus: persist everything to disk
    section("Saving data to disk")
    save_inventory(inventory, "data/vehicles.json")
    save_customers([customer_a, customer_b], "data/customers.json")
    print("Saved inventory and customers to the data/ folder.")


if __name__ == "__main__":
    main()