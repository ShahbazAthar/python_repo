import random
from payments.payment_processor import PaymentProcessor
from exceptions.rental_exceptions import PaymentFailureError, ValidationError


class UpiPaymentProcessor(PaymentProcessor):
    """Simulates a UPI / digital-wallet payment."""

    def __init__(self, upi_id):
        if not upi_id or "@" not in upi_id:
            raise ValidationError("UPI ID looks invalid (expected something like name@bank).")
        self.__upi_id = upi_id

    @property
    def upi_id(self):
        return self.__upi_id

    def process_payment(self, amount):
        print(f"Requesting Rs. {amount:,.0f} via UPI ({self.__upi_id})...")
        success = random.random() > 0.05
        if not success:
            raise PaymentFailureError("UPI payment request timed out or was declined.")
        print("Payment completed successfully.")
        return True