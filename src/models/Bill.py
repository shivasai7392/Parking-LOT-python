from src.models.BaseModel import BaseModel


class Bill(BaseModel):
    def __init__(self):
        self._ticket = None
        self._exit_time = None
        self._amount = None
        self._gate = None
        self._operator = None
        self._bill_status = None

    @property
    def ticket(self):
        return self._ticket

    @ticket.setter
    def ticket(self, value):
        self._ticket = value

    @property
    def exit_time(self):
        return self._exit_time

    @exit_time.setter
    def exit_time(self, value):
        self._exit_time = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def gate(self):
        return self._gate

    @gate.setter
    def gate(self, value):
        self._gate = value

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value

    @property
    def bill_status(self):
        return self._bill_status

    @bill_status.setter
    def bill_status(self, value):
        self._bill_status = value
