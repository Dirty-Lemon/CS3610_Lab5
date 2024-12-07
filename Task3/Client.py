from DirectorClass import Director
from CarBuilderClass import CarBuilder

theDirector = Director()
theBuilder = CarBuilder()
# theDirector.builder = theBuilder

print("Test for SUV:")
theDirector.makeSUV("Car builder", 3, "idk a big one")
theDirector.builder.product.showComponents()

print("Test for Sports Car:")
theDirector.makeSportsCar()
theBuilder.product.showComponents()