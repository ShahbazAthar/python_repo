class Invoice:
    """Builds and displays the final invoice for a Rental."""

    def __init__(self, rental):
        self.__rental = rental
        self.__base_amount = None
        self.__late_fee = None
        self.__final_amount = None

    def generate(self):
        self.__base_amount = self.__rental.base_amount()
        self.__late_fee = self.__rental.late_fee()
        self.__final_amount = self.__rental.calculate_final_amount()
        return self.__final_amount

    def display(self):
        if self.__final_amount is None:
            self.generate()

        vehicle = self.__rental.vehicle
        customer = self.__rental.customer

        print("----- INVOICE -----")
        print(f"Customer: {customer.name}")
        print(f"Selected vehicle: {vehicle.vehicle_id}")
        print(f"Rental duration: {self.__rental.rental_days} days")
        print(f"Base rental amount: Rs. {self.__base_amount:,.0f}")
        print(f"Insurance premium: Rs. {self.__rental.insurance_premium:,.0f}")
        print(f"Late fee: Rs. {self.__late_fee:,.0f}")
        print(f"Final amount: Rs. {self.__final_amount:,.0f}")
        print(f"Security deposit refunded: Rs. {self.__rental.security_deposit:,.0f}")
        print("--------------------")