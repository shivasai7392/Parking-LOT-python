from typing import List

from src.models.ParkingLot import ParkingLot
from src.models.ParkingSpot import ParkingSpot
from src.models.SpotStatus import SpotStatus
from src.models.VehicleType import VehicleType
from src.strategies.spotassignmentstrategies.ISpotAssigmentStrategy import ISpotAssignmentStrategy


class RandomSpotAssignmentStrategy(ISpotAssignmentStrategy):
    def findSpot(self, parking_lot: ParkingLot, vehicle_type: VehicleType) -> ParkingSpot:
        parking_floors = parking_lot.parkingFloors
        parking_spots: List[ParkingSpot] = parking_floors.parking_spots
        for parking_spot in parking_spots:
            if parking_spot.spot_status == SpotStatus.EMPTY and vehicle_type in parking_spot.supported_vehicle_types:
                return parking_spot


