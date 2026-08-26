import json
import os


class DataStore:
    """Generic JSON file read/write wrapper — the low-level persistence primitive."""

    def __init__(self, file_path):
        self.__file_path = file_path

    def save(self, data):
        directory = os.path.dirname(self.__file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load(self):
        if not os.path.exists(self.__file_path):
            return None
        with open(self.__file_path, "r", encoding="utf-8") as f:
            return json.load(f)


def save_inventory(inventory, file_path="data/vehicles.json"):
    store = DataStore(file_path)
    store.save([vehicle.to_dict() for vehicle in inventory.list_all()])


def load_inventory(file_path="data/vehicles.json"):
    from models.vehicle import Vehicle
    store = DataStore(file_path)
    records = store.load()
    if not records:
        return []
    return [Vehicle.from_dict(record) for record in records]


def save_customers(customers, file_path="data/customers.json"):
    store = DataStore(file_path)
    store.save([customer.to_dict() for customer in customers])


def load_customers(file_path="data/customers.json"):
    from models.customer import Customer
    store = DataStore(file_path)
    records = store.load()
    if not records:
        return []
    return [Customer.from_dict(record) for record in records]