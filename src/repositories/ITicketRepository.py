import abc

from src.models.Ticket import Ticket


class ITicketRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, ticket: Ticket) -> Ticket:
        pass

    @abc.abstractmethod
    def getByVehicleId(self, vehicle_id: int) -> Ticket:
        pass
