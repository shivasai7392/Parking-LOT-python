from datetime import datetime

from src.models.VehicleType import VehicleType
from src.strategies.feecalculationstrategies.IFeesCalculationStrategy import IFeesCalculationStrategy


class RandomFeesCalculationStrategy(IFeesCalculationStrategy):

    def calculateFees(self, current_time: datetime, entry_Time: datetime, vehicle_type: VehicleType):
        return ((current_time - entry_Time).total_seconds())*1.5


