class GenerateBillResponseDto:

    def __init__(self):
        self._bill_id = 0
        self._amount = 0
        self._ticket_id = 0
        self._exit_time = None
        self._operator_name = None
        self._status = None

    @property
    def bill_id(self):
        return self._bill_id

    @bill_id.setter
    def bill_id(self, value):
        self._bill_id = value

    @property
    def amount(self):
        return self._amount

    @amount
    def amount(self, value):
        self._amount = value

    @property
    def ticket_id(self):
        return self._ticket_id

    @ticket_id
    def ticket_id(self, value):
        self._ticket_id = value

    @property
    def exit_time(self):
        return self._exit_time

    @exit_time
    def exit_time(self, value):
        self._exit_time = value

    @property
    def operator_name(self):
        return self._operator_name

    @operator_name
    def operator_name(self, value):
        self._operator_name = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
