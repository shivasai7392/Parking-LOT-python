class GenerateTicketResponseDto:
    def __init__(self):
        self._ticket_id = None
        self._entry_time = None
        self._spot_number = None
        self._floor_number = None

    @property
    def ticket_id(self):
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, value):
        self._ticket_id = value

    @property
    def entry_time(self):
        return self._entry_time

    @entry_time.setter
    def entry_time(self, value):
        self._entry_time = value

    @property
    def spot_number(self):
        return self._spot_number

    @spot_number.setter
    def spot_number(self, value):
        self._spot_number = value

    @property
    def floor_number(self):
        return self._floor_number

    @floor_number.setter
    def floor_number(self, value):
        self._floor_number = value
