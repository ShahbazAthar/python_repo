from exceptions.rental_exceptions import ValidationError


class Admin:
    """
    Administrator role — manages inventory and vehicle maintenance status.
    Deliberately a separate class from Customer, not a subclass of it:
    an Admin isn't a specialized Customer, they're a different kind of
    actor with different permissions. Inheritance would be the wrong tool here.
    """

    def __init__(self, admin_id, name):
        if not name or not name.strip():
            raise ValidationError("Admin name cannot be empty.")
        self.__admin_id = admin_id
        self.__name = name

    @property
    def admin_id(self):
        return self.__admin_id

    @property
    def name(self):
        return self.__name

    def add_vehicle(self, inventory, vehicle):
        inventory.add_vehicle(vehicle)
        print(f"[Admin: {self.__name}] Added vehicle {vehicle.vehicle_id} to inventory.")

    def set_vehicle_maintenance(self, vehicle, flag):
        vehicle.set_under_maintenance(flag)
        state = "under maintenance" if flag else "available for rent"
        print(f"[Admin: {self.__name}] Marked {vehicle.vehicle_id} as {state}.")

    def view_all_rentals(self, rental_service):
        print(f"[Admin: {self.__name}] Viewing all rentals:")
        rental_service.display_all_rentals()