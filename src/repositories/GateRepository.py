from typing import Dict

from src.models.Gate import Gate
from src.repositories.IGateRepository import IGateRepository


class GateRepository(IGateRepository):

    def __init__(self):
        self.gates: Dict[int, Gate] = {4: Gate()}

    def getById(self, gateId: int):
        return self.gates[gateId] if gateId in self.gates else None
