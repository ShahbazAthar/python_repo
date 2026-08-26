from exceptions.rental_exceptions import ValidationError


class Customer:
    """Stores customer identity + rental history."""

    def __init__(self, customer_id, name, email, licence_number):
        if not name or not name.strip():
            raise ValidationError("Customer name cannot be empty.")
        if not email or "@" not in email:
            raise ValidationError("Customer email looks invalid.")
        if not licence_number or not licence_number.strip():
            raise ValidationError("Driving licence number cannot be empty.")

        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__licence_number = licence_number
        self.__rental_history = []

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def licence_number(self):
        return self.__licence_number

    def add_rental(self, rental):
        self.__rental_history.append(rental)

    def display_rental_history(self):
        if not self.__rental_history:
            print(f"{self.__name} has no rental history yet.")
            return
        print(f"Rental history for {self.__name}:")
        for rental in self.__rental_history:
            print(f"  {rental}")

    def to_dict(self):
        """Bonus: plain-dict form for JSON persistence. Rental history isn't
        persisted here — it's rebuilt from saved Rental records separately."""
        return {
            "customer_id": self.__customer_id,
            "name": self.__name,
            "email": self.__email,
            "licence_number": self.__licence_number,
        }

    @staticmethod
    def from_dict(data):
        return Customer(data["customer_id"], data["name"], data["email"], data["licence_number"])