from src.models.BaseModel import BaseModel


class ParkingLot(BaseModel):

    def __init__(self):
        self._capacity = 0
        self._parkingFloors = None
        self._gates = None

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    @property
    def parkingFloors(self):
        return self._parkingFloors

    @parkingFloors.setter
    def parkingFloors(self, value):
        self._parkingFloors = value

    @property
    def gates(self):
        return self._gates

    @gates.setter
    def gates(self, value):
        self._gates = value
