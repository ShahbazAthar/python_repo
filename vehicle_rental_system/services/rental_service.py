from models.rental import Rental
from models.invoice import Invoice
from exceptions.rental_exceptions import (
    VehicleUnavailableError,
    VehicleUnderMaintenanceError,
    PaymentFailureError,
)


class RentalService:
    """
    The orchestrator. Depends on PaymentProcessor (the interface) and
    VehicleInventory — never on a concrete payment or vehicle class.
    notification_service is optional so existing tests / callers that
    don't pass one keep working unchanged.
    """

    def __init__(self, inventory, notification_service=None):
        self.__inventory = inventory
        self.__rentals = []
        self.__next_rental_id = 1
        self.__notification_service = notification_service

    def rent_vehicle(self, customer, vehicle, days, payment_processor, rental_date=None):
        if vehicle.under_maintenance:
            raise VehicleUnderMaintenanceError(f"Vehicle {vehicle.vehicle_id} is under maintenance.")
        if not vehicle.available:
            raise VehicleUnavailableError(f"Vehicle {vehicle.vehicle_id} is not available.")

        base = vehicle.calculate_rental_cost(days)
        insurance = vehicle.calculate_insurance_premium(days)
        deposit = vehicle.calculate_security_deposit()
        total_due = base + insurance + deposit

        try:
            payment_processor.process_payment(total_due)
        except PaymentFailureError:
            if self.__notification_service:
                self.__notification_service.notify_payment_failed(customer)
            raise

        rental_id = f"R{self.__next_rental_id:03d}"
        self.__next_rental_id += 1

        rental = Rental(rental_id, customer, vehicle, days, rental_date=rental_date)
        self.__rentals.append(rental)

        if self.__notification_service:
            self.__notification_service.notify_rental_confirmed(customer, rental)

        return rental

    def return_vehicle(self, rental, return_date=None):
        rental.complete_rental(return_date)
        invoice = Invoice(rental)
        final_amount = invoice.generate()

        if self.__notification_service:
            self.__notification_service.notify_rental_returned(rental.customer, rental, final_amount)

        return invoice

    def cancel_rental(self, rental):
        refund_amount = rental.cancel_rental()
        print(f"Rental {rental.rental_id} cancelled. Refunding Rs. {refund_amount:,.0f} to {rental.customer.name}.")

        if self.__notification_service:
            self.__notification_service.notify_rental_cancelled(rental.customer, rental, refund_amount)

        return refund_amount

    def get_rental(self, rental_id):
        for rental in self.__rentals:
            if rental.rental_id == rental_id:
                return rental
        return None

    def list_active_rentals(self):
        return [r for r in self.__rentals if r.status == "active"]

    def display_all_rentals(self):
        if not self.__rentals:
            print("No rentals recorded yet.")
            return
        print("All rentals:")
        for rental in self.__rentals:
            print(f"  {rental}")