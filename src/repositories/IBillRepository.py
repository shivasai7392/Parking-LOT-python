import abc

from src.models.Bill import Bill


class IBillRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, bill: Bill) -> Bill:
        pass