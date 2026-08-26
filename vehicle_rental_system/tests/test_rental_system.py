import unittest
from datetime import date, timedelta

from models.vehicle import Car, Bike, Van
from models.customer import Customer
from models.rental import Rental
from services.vehicle_inventory import VehicleInventory
from services.rental_service import RentalService
from payments.payment_processor import PaymentProcessor
from exceptions.rental_exceptions import (
    ValidationError,
    InvalidRentalDurationError,
    VehicleUnavailableError,
    VehicleUnderMaintenanceError,
    PaymentFailureError,
)


# --- Test-only PaymentProcessor implementations, for deterministic testing ---

class AlwaysSucceedsPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return True


class AlwaysFailsPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        raise PaymentFailureError("Simulated failure for testing.")


class TestVehicleCostCalculation(unittest.TestCase):
    """Success paths: polymorphic calculate_rental_cost per vehicle type."""

    def test_car_cost_is_daily_rate_times_days(self):
        car = Car("V1", "REG1", "Toyota", "Innova", 2000)
        self.assertEqual(car.calculate_rental_cost(3), 6000)

    def test_bike_discount_applies_past_five_days(self):
        bike = Bike("V2", "REG2", "Yamaha", "FZ", 700)
        self.assertEqual(bike.calculate_rental_cost(7), 700 * 7 * 0.95)

    def test_bike_no_discount_at_exactly_five_days(self):
        bike = Bike("V2", "REG2", "Yamaha", "FZ", 700)
        self.assertEqual(bike.calculate_rental_cost(5), 700 * 5)

    def test_van_adds_service_charge(self):
        van = Van("V3", "REG3", "Tata", "Ace", 3000)
        self.assertEqual(van.calculate_rental_cost(2), (3000 * 2) + Van.SERVICE_CHARGE)


class TestVehicleValidation(unittest.TestCase):
    """Failure paths: Vehicle construction must reject bad data."""

    def test_empty_registration_number_rejected(self):
        with self.assertRaises(ValidationError):
            Car("V1", "", "Toyota", "Innova", 2000)

    def test_zero_daily_rate_rejected(self):
        with self.assertRaises(ValidationError):
            Car("V1", "REG1", "Toyota", "Innova", 0)

    def test_negative_daily_rate_rejected(self):
        with self.assertRaises(ValidationError):
            Car("V1", "REG1", "Toyota", "Innova", -500)


class TestCustomerValidation(unittest.TestCase):
    """Failure paths: Customer construction must reject bad data."""

    def test_empty_name_rejected(self):
        with self.assertRaises(ValidationError):
            Customer("C1", "", "a@b.com", "DL123")

    def test_invalid_email_rejected(self):
        with self.assertRaises(ValidationError):
            Customer("C1", "Ananya", "not-an-email", "DL123")

    def test_empty_licence_rejected(self):
        with self.assertRaises(ValidationError):
            Customer("C1", "Ananya", "a@b.com", "")

    def test_valid_customer_accepted(self):
        customer = Customer("C1", "Ananya", "a@b.com", "DL123")
        self.assertEqual(customer.name, "Ananya")


class TestRentalBusinessRules(unittest.TestCase):
    """Business rules from section 3 of the spec, both success and failure paths."""

    def setUp(self):
        self.car = Car("V1", "REG1", "Toyota", "Innova", 2000)
        self.customer = Customer("C1", "Ananya", "a@b.com", "DL123")

    def test_zero_days_rejected(self):
        with self.assertRaises(InvalidRentalDurationError):
            Rental("R1", self.customer, self.car, 0)

    def test_negative_days_rejected(self):
        with self.assertRaises(InvalidRentalDurationError):
            Rental("R1", self.customer, self.car, -2)

    def test_renting_unavailable_vehicle_rejected(self):
        Rental("R1", self.customer, self.car, 3)  # first rental succeeds, marks car unavailable
        other_customer = Customer("C2", "Rohan", "r@b.com", "DL999")
        with self.assertRaises(VehicleUnavailableError):
            Rental("R2", other_customer, self.car, 2)

    def test_maintenance_blocks_rental(self):
        self.car.set_under_maintenance(True)
        with self.assertRaises(VehicleUnderMaintenanceError):
            Rental("R1", self.customer, self.car, 3)

    def test_successful_rental_marks_vehicle_unavailable(self):
        Rental("R1", self.customer, self.car, 3)
        self.assertFalse(self.car.available)

    def test_late_fee_calculation(self):
        rental_date = date(2026, 8, 1)
        rental = Rental("R1", self.customer, self.car, 3, rental_date=rental_date)
        rental.complete_rental(return_date=rental_date + timedelta(days=4))  # 1 day late
        self.assertEqual(rental.late_days, 1)
        self.assertEqual(rental.late_fee(), 1 * (2000 * 0.20))
        self.assertEqual(rental.calculate_final_amount(), 6000 + 400 + rental.insurance_premium)

    def test_on_time_return_has_no_late_fee(self):
        rental_date = date(2026, 8, 1)
        rental = Rental("R1", self.customer, self.car, 3, rental_date=rental_date)
        rental.complete_rental(return_date=rental_date + timedelta(days=3))  # exactly on time
        self.assertEqual(rental.late_days, 0)
        self.assertEqual(rental.late_fee(), 0)

    def test_returned_vehicle_becomes_available(self):
        rental = Rental("R1", self.customer, self.car, 3)
        rental.complete_rental()
        self.assertTrue(self.car.available)

    def test_cancel_rental_refunds_and_frees_vehicle(self):
        rental = Rental("R1", self.customer, self.car, 3)
        refund = rental.cancel_rental()
        self.assertTrue(self.car.available)
        self.assertEqual(rental.status, "cancelled")
        self.assertGreater(refund, 0)


class TestRentalServicePaymentFlow(unittest.TestCase):
    """
    Confirms RentalService depends only on the PaymentProcessor interface —
    both a succeeding and a failing implementation work correctly, and
    payment failure prevents the rental from being created at all.
    """

    def setUp(self):
        self.inventory = VehicleInventory()
        self.car = Car("V1", "REG1", "Toyota", "Innova", 2000)
        self.inventory.add_vehicle(self.car)
        self.customer = Customer("C1", "Ananya", "a@b.com", "DL123")
        self.service = RentalService(self.inventory)

    def test_successful_payment_creates_rental(self):
        rental = self.service.rent_vehicle(self.customer, self.car, 3, AlwaysSucceedsPaymentProcessor())
        self.assertEqual(rental.status, "active")
        self.assertFalse(self.car.available)

    def test_failed_payment_blocks_rental_and_leaves_vehicle_available(self):
        with self.assertRaises(PaymentFailureError):
            self.service.rent_vehicle(self.customer, self.car, 3, AlwaysFailsPaymentProcessor())
        self.assertTrue(self.car.available)  # vehicle must NOT be marked rented


class TestVehicleInventorySearch(unittest.TestCase):

    def setUp(self):
        self.inventory = VehicleInventory()
        self.inventory.add_vehicle(Car("V1", "REG1", "Toyota", "Innova", 2000))
        self.inventory.add_vehicle(Bike("V2", "REG2", "Yamaha", "FZ", 700))
        self.inventory.add_vehicle(Van("V3", "REG3", "Tata", "Ace", 3000))

    def test_search_by_type(self):
        results = self.inventory.search_vehicles(vehicle_type="Bike")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].vehicle_id, "V2")

    def test_search_by_max_price(self):
        results = self.inventory.search_vehicles(max_price=1000)
        self.assertEqual(len(results), 1)  # only the bike qualifies at <= 1000

    def test_search_by_type_and_price_combined(self):
        results = self.inventory.search_vehicles(vehicle_type="Car", max_price=2500)
        self.assertEqual(len(results), 1)


if __name__ == "__main__":
    unittest.main()