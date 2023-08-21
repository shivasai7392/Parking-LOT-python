# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.controllers.TicketController import TicketController
from src.dtos.GenerateTicketRequestDto import GenerateTicketRequestDto
from src.dtos.GenerateTicketResponseDto import GenerateTicketResponseDto
from src.models.VehicleType import VehicleType
from src.repositories.GateRepository import GateRepository
from src.repositories.ParkingLotRepository import ParkingLotRepository
from src.repositories.TicketRepoistory import TicketRepository
from src.repositories.VehicleRepository import VehicleRepository
from src.services.TicketService import TicketService
from src.strategies.spotassignmentstrategies.RandomSpotAssignmentStrategy import RandomSpotAssignmentStrategy


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    gate_repository = GateRepository()
    parking_lot_repository = ParkingLotRepository()
    vehicle_repository = VehicleRepository()
    ticket_repository = TicketRepository()

    random_spot_assignment_strategy = RandomSpotAssignmentStrategy()

    ticket_service = TicketService(vehicle_repository, gate_repository, random_spot_assignment_strategy,
                                   parking_lot_repository, ticket_repository)

    ticket_controller = TicketController(ticket_service)

    request: GenerateTicketRequestDto = GenerateTicketRequestDto()
    request.gate_id = 4
    request.vehicle_registration_number = "APNE001234"
    request.vehicle_type = VehicleType.CAR
    response: GenerateTicketResponseDto = ticket_controller.generateTicket(request)

    print(response.status)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
