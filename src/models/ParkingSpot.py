from src.models.BaseModel import BaseModel


class ParkingSpot(BaseModel):
    def __init__(self):
        self._spot_number = 0
        self._supported_vehicle_types = None
        self._spot_status = None
        self._parking_floor = 0

    @property
    def spot_number(self):
        return self._spot_number

    @spot_number.setter
    def spot_number(self, value):
        self._spot_number = value

    @property
    def parking_floor(self):
        return self._spot_number

    @parking_floor.setter
    def parking_floor(self, value):
        self._parking_floor = value

    @property
    def supported_vehicle_types(self):
        return self._supported_vehicle_types

    @supported_vehicle_types.setter
    def supported_vehicle_types(self, value):
        self._supported_vehicle_types = value

    @property
    def spot_status(self):
        return self._spot_status

    @spot_status.setter
    def spot_status(self, value):
        self._spot_status = value
