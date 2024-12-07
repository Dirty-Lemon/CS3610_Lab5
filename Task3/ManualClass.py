# from CarManualBuilderClass import CarManualBuilder

class Manual:
    def __init__(self)-> None:
        self.__name = "Car Manual"
        self.__components = []
    
    def add(self, component)-> None:
        print(f"The component {component} is being added now...")
        self.__components.append(component)
        print(self.__components)
    
    def showComponents(self)-> None:
        print(f"There is/are {len(self.__components)} component(s) in the {self.__name}")
        print(f"The component of {self.__name} are:")
        for item in self.__components:
            print(item)