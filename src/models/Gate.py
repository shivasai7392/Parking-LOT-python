from src.models.BaseModel import BaseModel


class Gate(BaseModel):
    def __init__(self):
        self._gate_number = 0
        self._operator = None
        self._gate_status = None
        self._gate_type = None

    @property
    def gate_number(self):
        return self._gate_number

    @gate_number.setter
    def gate_number(self, value):
        self._gate_number = value

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value

    @property
    def gate_status(self):
        return self._gate_status

    @gate_status.setter
    def gate_status(self, value):
        self._gate_status = value

    @property
    def gate_type(self):
        return self._gate_type

    @gate_type.setter
    def gate_type(self, value):
        self._gate_type = value
