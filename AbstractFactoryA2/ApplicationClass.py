from AbstractFactoryA2.MacFactoryClass import MacFactory
from AbstractFactoryA2.WinFactoryClass import WinFactory
from AbstractFactoryA2.IGUIFactoryClass import IGUIFactory

class Application():
    def __init__(self, factory: IGUIFactory):
        self.__factory= factory
        self.__button = None
        self.__checkbox = None

    def createUI(self):
        self.__button = self.__factory.createButton()
        self.__checkbox = self.__factory.createCheckbox()
        return f"\n Button: {self.__button.get_button()}, \n Checkbox: {self.__checkbox.get_checkbox()}"

    def paint(self):
       print ("\n I am a painting!!")
       return None
