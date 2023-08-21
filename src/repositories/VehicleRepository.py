from typing import Dict

from src.models import Vehicle
from src.repositories.IVehicleRepository import IVehicleRepository


class VehicleRepository(IVehicleRepository):

    def __init__(self):
        self.generated_id: int = 0
        self.vehicles: Dict[int, Vehicle] = dict()
        self.vehicles_by_number: Dict[str, Vehicle] = dict()

    def getByVehicleNumber(self, vehicle_registration_number):
        return self.vehicles_by_number[vehicle_registration_number] if vehicle_registration_number in self.vehicles_by_number else None

    def save(self, vehicle: Vehicle):
        self.generated_id += 1
        vehicle.id = self.generated_id
        self.vehicles[self.generated_id] = vehicle
        return vehicle
