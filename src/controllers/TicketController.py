from src.dtos.GenerateTicketRequestDto import GenerateTicketRequestDto
from src.dtos.GenerateTicketResponseDto import GenerateTicketResponseDto
from src.dtos.ResponseStatus import ResponseStatus
from src.exceptions.InvalidArgumentException import InvalidArgumentException
from src.models.Ticket import Ticket
from src.services.TicketService import TicketService


class TicketController:

    def __init__(self, ticket_service: TicketService):
        self.ticket_service = ticket_service

    def generateTicket(self, request: GenerateTicketRequestDto) -> GenerateTicketResponseDto:
        response: GenerateTicketResponseDto = GenerateTicketResponseDto()

        try:
            generated_ticket: Ticket = self.ticket_service.generateTicket(request.vehicle_registration_number,
                                                                          request.gate_id, request.vehicle_type)
        except InvalidArgumentException:
            print("Fail")
            response.status = ResponseStatus.FAILURE
            return response

        response.ticket_id = generated_ticket.ticket_id
        response.entry_time = generated_ticket.entry_time
        response.spot_number = generated_ticket.parking_spot.spot_number
        response.floor_number = generated_ticket.parking_spot.parking_floor.floor_number
        response.status = ResponseStatus.SUCCESS

        return response
