import abc
from datetime import datetime

from src.models.VehicleType import VehicleType


class IFeesCalculationStrategy(abc.ABC):
    @abc.abstractmethod
    def calculateFees(self, current_time: datetime, entry_time: datetime, vehicle_type: VehicleType):
        pass
