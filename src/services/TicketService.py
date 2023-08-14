import datetime

from src.exceptions.InvalidArgumentException import InvalidArgumentException
from src.models.Gate import Gate
from src.models.ParkingLot import ParkingLot
from src.models.ParkingSpot import ParkingSpot
from src.models.SpotStatus import SpotStatus
from src.models.Ticket import Ticket
from src.models.Vehicle import Vehicle
from src.models.VehicleType import VehicleType
from src.repositories.IGateRepository import IGateRepository
from src.repositories.IParkingLotRepository import IParkingLotRepository
from src.repositories.ITicketRepository import ITicketRepository
from src.repositories.IVehicleRepository import IVehicleRepository
from src.strategies.spotassignmentstrategies.ISpotAssigmentStrategy import ISpotAssignmentStrategy


class TicketService:

    def __init__(self, vehicle_repository: IVehicleRepository,
                 gate_repository: IGateRepository,
                 spot_assignment_strategy: ISpotAssignmentStrategy,
                 parking_lot_repository: IParkingLotRepository,
                 ticket_repository: ITicketRepository):
        self.vehicle_repository = vehicle_repository
        self.gate_repository = gate_repository
        self.spot_assignment_strategy = spot_assignment_strategy
        self.parking_lot_repository = parking_lot_repository
        self.ticket_repository = ticket_repository

    def generateTicket(self, vehicle_registration_number: str, gate_id: int, vehicle_type: VehicleType) -> Ticket:
        vehicle: Vehicle = self.vehicle_repository.vehicles_by_number(vehicle_registration_number)
        if vehicle is None:
            vehicle = Vehicle()
            vehicle.vehicle_type = vehicle_type
            vehicle.registration_number = vehicle_registration_number
            vehicle = self.vehicle_repository.save(vehicle)

        gate: Gate = self.gate_repository.getGateById(gate_id)
        if gate is None:
            raise InvalidArgumentException("No gate with id {} is available".format(str(gate_id)))

        parking_lot: ParkingLot = self.parking_lot_repository.getParkingLotByGateId(gate_id)
        if parking_lot is None:
            raise InvalidArgumentException("No parking lot is available")

        parking_spot: ParkingSpot = self.spot_assignment_strategy.findSpot(parking_lot, vehicle_type)
        if parking_spot is None:
            raise InvalidArgumentException("No parking lot is available")

        ticket: Ticket = Ticket()
        ticket.vehicle = vehicle
        ticket.gate = gate
        ticket.entry_time = datetime.datetime.now()
        ticket.operator = gate.operator
        parking_spot.spot_status = SpotStatus.FILLED
        ticket.parking_spot = parking_spot

        ticket: Ticket = self.ticket_repository.save(ticket)

        return ticket
