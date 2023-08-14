from src.models.BaseModel import BaseModel


class Ticket(BaseModel):
    def __init__(self):
        self._parking_spot = None
        self._entry_time = None
        self._vehicle = None
        self._operator = None
        self._gate = None

    @property
    def parking_spot(self):
        return self._parking_spot

    @parking_spot.setter
    def parking_spot(self, value):
        self._parking_spot = value

    @property
    def entry_time(self):
        return self._entry_time

    @entry_time.setter
    def entry_time(self, value):
        self._entry_time = value

    @property
    def vehicle(self):
        return self._vehicle

    @vehicle.setter
    def vehicle(self, value):
        self._vehicle = value

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value

    @property
    def gate(self):
        return self._gate

    @gate.setter
    def gate(self, value):
        self._gate = value
