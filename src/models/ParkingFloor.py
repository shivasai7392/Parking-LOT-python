from src.models.BaseModel import BaseModel


class ParkingFloor(BaseModel):
    def __init__(self):
        self._floor_number = 0
        self._parking_spots = None
        self._parking_lot = None

    @property
    def floor_number(self):
        return self._floor_number

    @floor_number.setter
    def floor_number(self, value):
        self._floor_number = value

    @property
    def parking_spots(self):
        return self._parking_spots

    @parking_spots.setter
    def parking_spots(self, value):
        self._parking_spots = value

    @property
    def parking_lot(self):
        return self._parking_lot

    @parking_lot.setter
    def parking_lot(self, value):
        self._parking_lot = value
    