from enum import Enum


class BillStatus(Enum):
    SUCCESS = 1,
    FAILURE = 2,
    PENDING = 3,
