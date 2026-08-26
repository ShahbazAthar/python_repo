class VehicleInventory:
    """Owns the master list of vehicles and answers search/availability queries."""

    def __init__(self):
        self.__vehicles = []

    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)

    def list_available(self):
        return [v for v in self.__vehicles if v.available]

    def list_all(self):
        return list(self.__vehicles)

    def display_available(self):
        print("Available Vehicles")
        print("-" * 50)
        for vehicle in self.list_available():
            vehicle.display_details()

    def search_vehicles(self, vehicle_type=None, max_price=None):
        """
        One method, multiple ways to search — the Pythonic substitute for
        method overloading (Python doesn't support true overloading).
        """
        results = self.__vehicles
        if vehicle_type is not None:
            results = [v for v in results if type(v).__name__.lower() == vehicle_type.lower()]
        if max_price is not None:
            results = [v for v in results if v.daily_rate <= max_price]
        return results

    def get_vehicle(self, vehicle_id):
        for vehicle in self.__vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None