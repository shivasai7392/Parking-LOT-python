from typing import Dict

from src.models.Bill import Bill
from src.repositories.IBillRepository import IBillRepository


class BillRepository(IBillRepository):

    def __init__(self):
        self.bills: Dict[int, Bill] = dict()
        self.generated_id = 0

    def save(self, bill: Bill) -> Bill:
        self.generated_id += 1
        bill.id = self.generated_id
        self.bills[bill.id] = bill
        return bill
