import abc

from src.models.Vehicle import Vehicle


class IVehicleRepository(abc.ABC):
    @abc.abstractmethod
    def getByVehicleNumber(self, vehicle_registration_number: str):
        pass

    @abc.abstractmethod
    def save(self, vehicle: Vehicle):
        pass