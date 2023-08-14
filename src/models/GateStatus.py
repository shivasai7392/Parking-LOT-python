from enum import Enum


class GateStatus(Enum):
    OPEN = 1,
    CLOSED = 2,
    SHUTDOWN = 3,
