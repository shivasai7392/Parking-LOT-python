from typing import Dict

from src.models.ParkingLot import ParkingLot
from src.repositories.IParkingLotRepository import IParkingLotRepository


class ParkingLotRepository(IParkingLotRepository):

    def __init__(self):
        self.parking_lots: Dict[int, ParkingLot] = dict()
        self.parking_lots_with_gateId: Dict[int, ParkingLot] = dict()

    def getParkingLotByGateId(self, gateId: int):
        return self.parking_lots_with_gateId[gateId] if gateId in self.parking_lots_with_gateId else None
