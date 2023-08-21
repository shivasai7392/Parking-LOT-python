class GenerateTicketRequestDto:

    def __init__(self):
        self._vehicle_registration_number = None
        self._gate_id = None
        self._vehicle_type = None

    @property
    def vehicle_registration_number(self):
        return self._vehicle_registration_number

    @vehicle_registration_number.setter
    def vehicle_registration_number(self, value):
        self._vehicle_registration_number = value

    @property
    def gate_id(self):
        return self._gate_id

    @gate_id.setter
    def gate_id(self, value):
        self._gate_id = value

    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value
