from typing import Dict

from src.models.Ticket import Ticket
from src.repositories.ITicketRepository import ITicketRepository


class TicketRepository(ITicketRepository):

    def __init__(self):
        self.tickets: Dict[int, Ticket] = dict()
        self.generated_id = 0

    def save(self, ticket: Ticket) -> Ticket:
        self.generated_id += 1
        ticket.id = self.generated_id
        self.tickets[ticket.id] = ticket
        return ticket
