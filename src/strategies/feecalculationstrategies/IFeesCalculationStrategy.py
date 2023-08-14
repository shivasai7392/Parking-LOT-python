import abc


class IFeesCalculationStrategy(abc.ABC):
    @abc.abstractmethod
    def calculateFees(self):
        pass
