from datetime import date, timedelta
from exceptions.rental_exceptions import (
    InvalidRentalDurationError,
    VehicleUnavailableError,
    VehicleUnderMaintenanceError,
    InvalidOperationError,
)

LATE_FEE_RATE = 0.20        # 20% of daily rate, per late day
CANCELLATION_FEE_RATE = 0.10  # 10% of base amount forfeited on cancellation


class Rental:
    """Composition: a Rental HAS-A Customer, HAS-A Vehicle."""

    def __init__(self, rental_id, customer, vehicle, rental_days, rental_date=None):
        if rental_days <= 0:
            raise InvalidRentalDurationError("Rental days must be greater than zero.")
        if vehicle.under_maintenance:
            raise VehicleUnderMaintenanceError(
                f"Vehicle {vehicle.vehicle_id} is under maintenance and cannot be rented."
            )
        if not vehicle.available:
            raise VehicleUnavailableError(
                f"Vehicle {vehicle.vehicle_id} is not available for rent."
            )

        self.__rental_id = rental_id
        self.__customer = customer
        self.__vehicle = vehicle
        self.__rental_days = rental_days
        self.__rental_date = rental_date or date.today()
        self.__due_date = self.__rental_date + timedelta(days=rental_days)
        self.__return_date = None
        self.__late_days = 0
        self.__status = "active"

        self.__security_deposit = vehicle.calculate_security_deposit()
        self.__insurance_premium = vehicle.calculate_insurance_premium(rental_days)

        vehicle.mark_as_rented()
        customer.add_rental(self)

    @property
    def rental_id(self):
        return self.__rental_id

    @property
    def customer(self):
        return self.__customer

    @property
    def vehicle(self):
        return self.__vehicle

    @property
    def rental_days(self):
        return self.__rental_days

    @property
    def status(self):
        return self.__status

    @property
    def late_days(self):
        return self.__late_days

    @property
    def due_date(self):
        return self.__due_date

    @property
    def security_deposit(self):
        return self.__security_deposit

    @property
    def insurance_premium(self):
        return self.__insurance_premium

    def base_amount(self):
        return self.__vehicle.calculate_rental_cost(self.__rental_days)

    def late_fee(self):
        return self.__late_days * (self.__vehicle.daily_rate * LATE_FEE_RATE)

    def total_upfront_amount(self):
        """What gets charged at rental time: base + insurance + refundable deposit."""
        return self.base_amount() + self.__insurance_premium + self.__security_deposit

    def calculate_final_amount(self):
        """Final settlement at return: base + late fee + insurance (deposit is refunded separately)."""
        return self.base_amount() + self.late_fee() + self.__insurance_premium

    def complete_rental(self, return_date=None):
        if self.__status != "active":
            raise InvalidOperationError(f"Rental {self.__rental_id} cannot be returned (status={self.__status}).")

        self.__return_date = return_date or date.today()
        self.__late_days = max(0, (self.__return_date - self.__due_date).days)

        self.__vehicle.mark_as_available()
        self.__status = "completed"

    def cancel_rental(self):
        """Bonus: cancel before/without ever returning. Forfeits a cancellation fee, refunds the rest."""
        if self.__status != "active":
            raise InvalidOperationError(f"Rental {self.__rental_id} cannot be cancelled (status={self.__status}).")

        cancellation_fee = self.base_amount() * CANCELLATION_FEE_RATE
        refund_amount = (self.base_amount() - cancellation_fee) + self.__insurance_premium + self.__security_deposit

        self.__vehicle.mark_as_available()
        self.__status = "cancelled"
        return refund_amount

    def __str__(self):
        return (f"Rental {self.__rental_id}: {self.__vehicle.brand} {self.__vehicle.model} "
                f"for {self.__rental_days} days, status={self.__status}")