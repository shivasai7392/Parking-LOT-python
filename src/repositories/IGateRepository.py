import abc


class IGateRepository(abc.ABC):

    @abc.abstractmethod
    def getById(self, gateId: int):
        pass
    