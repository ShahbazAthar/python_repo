import random
from payments.payment_processor import PaymentProcessor
from exceptions.rental_exceptions import PaymentFailureError, ValidationError


class CardPaymentProcessor(PaymentProcessor):
    """Simulates a card payment. Never stores the raw card number."""

    def __init__(self, card_number, card_holder_name):
        if not card_number or len(card_number.replace(" ", "")) < 12:
            raise ValidationError("Card number looks invalid.")
        if not card_holder_name or not card_holder_name.strip():
            raise ValidationError("Card holder name cannot be empty.")

        digits = card_number.replace(" ", "")
        self.__masked_card_number = "**** **** **** " + digits[-4:]
        self.__card_holder_name = card_holder_name

    @property
    def masked_card_number(self):
        return self.__masked_card_number

    def process_payment(self, amount):
        print(f"Charging Rs. {amount:,.0f} to card {self.__masked_card_number}...")
        success = random.random() > 0.05  # simulate ~95% success rate
        if not success:
            raise PaymentFailureError("Card payment was declined by the bank.")
        print("Payment completed successfully.")
        return True