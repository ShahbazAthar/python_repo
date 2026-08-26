from abc import ABC, abstractmethod
from exceptions.rental_exceptions import ValidationError


class Vehicle(ABC):
    """Abstract base class for every rentable vehicle."""

    SECURITY_DEPOSIT_MULTIPLIER = 2
    INSURANCE_RATE = 0.05

    def __init__(self, vehicle_id, registration_number, brand, model, daily_rate):
        if not registration_number or not registration_number.strip():
            raise ValidationError("Registration number cannot be empty.")
        if not brand or not brand.strip():
            raise ValidationError("Brand cannot be empty.")
        if not model or not model.strip():
            raise ValidationError("Model cannot be empty.")
        if daily_rate <= 0:
            raise ValidationError("Daily rate must be greater than zero.")

        self.__vehicle_id = vehicle_id
        self.__registration_number = registration_number
        self.__brand = brand
        self.__model = model
        self.__daily_rate = daily_rate
        self.__available = True
        self.__under_maintenance = False

    @property
    def vehicle_id(self):
        return self.__vehicle_id

    @property
    def registration_number(self):
        return self.__registration_number

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def daily_rate(self):
        return self.__daily_rate

    @property
    def available(self):
        return self.__available

    @property
    def under_maintenance(self):
        return self.__under_maintenance

    @abstractmethod
    def calculate_rental_cost(self, days):
        raise NotImplementedError

    def calculate_security_deposit(self):
        return self.__daily_rate * self.SECURITY_DEPOSIT_MULTIPLIER

    def calculate_insurance_premium(self, days):
        return self.calculate_rental_cost(days) * self.INSURANCE_RATE

    def display_details(self):
        if self.__under_maintenance:
            status = "Under maintenance"
        elif self.__available:
            status = "Available"
        else:
            status = "Rented"
        print(f"{self.__vehicle_id} | {type(self).__name__} | {self.__brand} {self.__model} "
              f"| Rs. {self.__daily_rate:,.0f} per day | {status}")

    def mark_as_rented(self):
        self.__available = False

    def mark_as_available(self):
        self.__available = True

    def set_under_maintenance(self, flag):
        self.__under_maintenance = bool(flag)
        if flag:
            self.__available = False

    def to_dict(self):
        """Bonus: plain-dict form for JSON persistence."""
        return {
            "type": type(self).__name__,
            "vehicle_id": self.__vehicle_id,
            "registration_number": self.__registration_number,
            "brand": self.__brand,
            "model": self.__model,
            "daily_rate": self.__daily_rate,
            "available": self.__available,
            "under_maintenance": self.__under_maintenance,
        }

    @staticmethod
    def from_dict(data):
        """Rebuilds the correct subclass (Car/Bike/Van) from a saved dict."""
        vehicle_classes = {"Car": Car, "Bike": Bike, "Van": Van}
        vehicle_class = vehicle_classes[data["type"]]
        vehicle = vehicle_class(
            data["vehicle_id"], data["registration_number"],
            data["brand"], data["model"], data["daily_rate"],
        )
        if not data.get("available", True):
            vehicle.mark_as_rented()
        if data.get("under_maintenance", False):
            vehicle.set_under_maintenance(True)
        return vehicle


class Car(Vehicle):
    SECURITY_DEPOSIT_MULTIPLIER = 2

    def calculate_rental_cost(self, days):
        return self.daily_rate * days


class Bike(Vehicle):
    DISCOUNT_THRESHOLD_DAYS = 5
    DISCOUNT_RATE = 0.05
    SECURITY_DEPOSIT_MULTIPLIER = 1

    def calculate_rental_cost(self, days):
        base = self.daily_rate * days
        if days > self.DISCOUNT_THRESHOLD_DAYS:
            return base * (1 - self.DISCOUNT_RATE)
        return base


class Van(Vehicle):
    SERVICE_CHARGE = 500
    SECURITY_DEPOSIT_MULTIPLIER = 3

    def calculate_rental_cost(self, days):
        return (self.daily_rate * days) + self.SERVICE_CHARGE