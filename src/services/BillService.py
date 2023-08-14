from datetime import datetime

from src.exceptions.InvalidArgumentException import InvalidArgumentException
from src.models.Bill import Bill
from src.models.BillStatus import BillStatus
from src.models.Gate import Gate
from src.models.SpotStatus import SpotStatus
from src.models.Ticket import Ticket
from src.models.Vehicle import Vehicle
from src.repositories.IBillRepository import IBillRepository
from src.repositories.IGateRepository import IGateRepository
from src.repositories.ITicketRepository import ITicketRepository
from src.strategies.feecalculationstrategies.IFeesCalculationStrategy import IFeesCalculationStrategy


class BillService:

    def __init__(self, ticket_repository: ITicketRepository,
                 random_fees_calculation_strategy: IFeesCalculationStrategy,
                 gate_repository: IGateRepository,
                 bill_repository: IBillRepository):
        self.ticket_repository = ticket_repository
        self.random_fees_calculation_strategy = random_fees_calculation_strategy
        self.gate_repository = gate_repository
        self.bill_repository = bill_repository

    def generateBill(self, vehicle_id: int, gate_id: int):
        ticket: Ticket = self.ticket_repository.getTicketByVehicleId(vehicle_id)
        if ticket is None:
            raise InvalidArgumentException()

        gate: Gate = self.gate_repository.getGateById(gate_id)
        if gate is None:
            raise InvalidArgumentException()

        entry_time = ticket.entry_time
        exit_time = datetime.now()
        vehicle: Vehicle = ticket.vehicle

        amount: int = self.random_fees_calculation_strategy.calculateFees(exit_time, entry_time, vehicle.vehicle_type)

        bill: Bill = Bill()
        bill.ticket = ticket
        bill.ticket.parking_spot.spot_status = SpotStatus.EMPTY
        bill.bill_status = BillStatus.PENDING
        bill.exit_time = exit_time
        bill.gate = gate
        bill.amount = amount
        bill.operator = gate.operator

        bill: Bill = self.bill_repository.save(bill)

        return bill

