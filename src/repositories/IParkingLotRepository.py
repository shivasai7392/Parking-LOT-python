import abc


class IParkingLotRepository(abc.ABC):

    @abc.abstractmethod
    def getParkingLotByGateId(self, gateId: int):
        pass
