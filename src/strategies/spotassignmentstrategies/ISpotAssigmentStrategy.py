import abc

from src.models.ParkingLot import ParkingLot
from src.models.ParkingSpot import ParkingSpot
from src.models.VehicleType import VehicleType


class ISpotAssignmentStrategy(abc.ABC):
    @abc.abstractmethod
    def findSpot(self, parking_lot: ParkingLot, vehicle_type: VehicleType) -> ParkingSpot:
        pass
