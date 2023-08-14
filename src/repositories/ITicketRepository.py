import abc

from src.models.Ticket import Ticket


class ITicketRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, ticket: Ticket) -> Ticket:
        pass
