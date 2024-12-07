from AbstractFactoryA2.MacButtonClass import MacButton
from AbstractFactoryA2.MacCheckBoxClass import MacCheckbox
from AbstractFactoryA2.IButtonClass import IButton
from AbstractFactoryA2.ICheckboxClass import ICheckbox
from AbstractFactoryA2.IGUIFactoryClass import IGUIFactory

class MacFactory(IGUIFactory):  
    '''
    The Concrete mac Factory Class
    '''
    def createButton(self)->IButton:       
            return MacButton()

    def createCheckbox(self)-> ICheckbox: 
            return MacCheckbox()