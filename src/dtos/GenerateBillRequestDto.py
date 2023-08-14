class GenerateBillRequestDto:

    def __init__(self):
        self._vehicle_id = None
        self._gate_id = None

    @property
    def vehicle_id(self):
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, value):
        self._vehicle_id = value

    @property
    def gate_id(self):
        return self._gate_id

    @gate_id.setter
    def gate_id(self, value):
        self._gate_id = value
