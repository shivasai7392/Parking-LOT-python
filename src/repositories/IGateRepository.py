import abc


class IGateRepository(abc.ABC):

    @abc.abstractmethod
    def getGateById(self, gateId: int):
        pass
    