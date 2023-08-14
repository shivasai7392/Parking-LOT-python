from src.dtos.GenerateBillRequestDto import GenerateBillRequestDto
from src.dtos.GenerateBillResponseDto import GenerateBillResponseDto
from src.dtos.ResponseStatus import ResponseStatus
from src.exceptions.InvalidArgumentException import InvalidArgumentException
from src.models.Bill import Bill
from src.services.BillService import BillService


class BillController:

    def __init__(self, bill_service: BillService):
        self.bill_service = bill_service

    def generateBill(self, request: GenerateBillRequestDto) -> GenerateBillResponseDto:
        response = GenerateBillResponseDto()
        try:
            bill: Bill = self.bill_service.generateBill(request.vehicle_id, request.gate_id)
        except InvalidArgumentException:
            print("Fail")
            response.status = ResponseStatus.FAILURE
            return response

        response.bill_id = bill.id
        response.amount = bill.amount
        response.ticket_id = bill.ticket.id
        response.operator_name = bill.operator.name
        response.exit_time = bill.exit_time
        response.status = ResponseStatus.SUCCESS

        return response
