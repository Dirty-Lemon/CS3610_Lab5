from typing import Type
from IBuilderClass import IBuilder

class Director:
    def __init__(self)-> None:
        self.__builder = None

    @property
    def builder(self)-> IBuilder:
        return self.__builder

    @builder.setter
    def builder(self, builder: Type[IBuilder])-> None:
        self.__builder = builder
        
    def makeSUV(self, builderType: str, number: int, engine)-> None:
        self.builder.setSeats(number)
        self.builder.setEngine(engine)
        self.builder.setTripComputer()
        self.builder.setGPS()

    def makeSportsCar(self, builderType: str, number: int, engine)-> None:
            self.builder.setSeats(number)
            self.builder.setEngine(engine)
            self.builder.setTripComputer()
            self.builder.setGPS()