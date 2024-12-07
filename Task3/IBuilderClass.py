from abc import ABC, abstractmethod

'''The Builder interface specifies methods 
for creating the different parts of the Product objects.'''

class IBuilder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:  #getResult method
        pass

    @abstractmethod
    def setSeats(self, number) -> None:
        pass

    @abstractmethod
    def setEngine(self, engine) -> None:
        pass

    @abstractmethod
    def setTripComputer(self) -> None:
        pass

    @abstractmethod
    def setGPS(self) -> None:
        pass