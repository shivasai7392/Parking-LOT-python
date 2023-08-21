import abc


class IParkingLotRepository(abc.ABC):

    @abc.abstractmethod
    def getByGateId(self, gateId: int):
        pass
