from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    """Contract every payment method must implement."""

    @abstractmethod
    def process_payment(self, amount):
        """Return True on success, raise PaymentFailureError on failure."""
        raise NotImplementedError