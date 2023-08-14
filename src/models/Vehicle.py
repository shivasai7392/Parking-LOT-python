from src.models.BaseModel import BaseModel


class Vehicle(BaseModel):
    def __init__(self):
        self._registration_number = None
        self._vehicle_type = None

    @property
    def registration_number(self):
        return self._registration_number

    @registration_number.setter
    def registration_number(self, value):
        self._registration_number = value

    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value
