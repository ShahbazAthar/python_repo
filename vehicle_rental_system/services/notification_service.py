"""
Notification simulation

Doesn't send anything real — just prints what WOULD be sent, so the
rental workflow's notification points are demonstrated without needing
an actual email/SMS provider.
"""


class NotificationService:
    def notify_rental_confirmed(self, customer, rental):
        print(f"[Notification] SMS to {customer.name}: Your rental {rental.rental_id} "
              f"for {rental.vehicle.brand} {rental.vehicle.model} is confirmed.")

    def notify_rental_returned(self, customer, rental, invoice_amount):
        print(f"[Notification] Email to {customer.email}: Rental {rental.rental_id} returned. "
              f"Final amount charged: Rs. {invoice_amount:,.0f}. Thank you for renting with us!")

    def notify_rental_cancelled(self, customer, rental, refund_amount):
        print(f"[Notification] SMS to {customer.name}: Rental {rental.rental_id} cancelled. "
              f"Rs. {refund_amount:,.0f} refunded.")

    def notify_payment_failed(self, customer):
        print(f"[Notification] SMS to {customer.name}: Your recent payment attempt failed. "
              f"Please try again.")