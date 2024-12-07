from ManualClass import Manual
from IBuilderClass import IBuilder

class CarManualBuilder(IBuilder):
    
    def __init__(self)-> None:
        self.reset()
        
    def reset(self)-> None:
        print("We have our initial Manual")
        self.__product = Manual()
        
    @property
    def product(self)-> Manual:
        currentManual = self.__product

        self.reset()    # ready to start producing a new car
        return currentManual
    
    
    def setSeats(self, number)-> None:
        for seat in number:
            self.__product.add(f"Seat {seat}")

    def setEngine(self, engine)-> None:
        self.__product.add("Engine")

    def setTripComputer(self)-> None:
        self.__product.add("Trip Computer")

    def setGPS(self)-> None:
        self.__product.add("GPS")