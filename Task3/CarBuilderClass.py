from CarClass import Car
from IBuilderClass import IBuilder

class CarBuilder(IBuilder):
    
    def __init__(self)-> None:
        self.reset()
        
    def reset(self)-> None:
        print("We have our initial Car")
        self.__product = Car()
        
    @property
    def product(self)-> Car:
        currentCar = self.__product

        self.reset()    # ready to start producing a new car
        return currentCar
    
    
    def setSeats(self, number)-> None:
        for seat in number:
            self.__product.add(f"Seat {seat}")

    def setEngine(self, engine)-> None:
        self.__product.add("Engine")

    def setTripComputer(self)-> None:
        self.__product.add("Trip Computer")

    def setGPS(self)-> None:
        self.__product.add("GPS")