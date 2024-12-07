from AbstractFactoryA2.WinButtonClass import WinButton
from AbstractFactoryA2.WinCheckBoxClass import WinCheckbox
from AbstractFactoryA2.IButtonClass import IButton
from AbstractFactoryA2.ICheckboxClass import ICheckbox
from AbstractFactoryA2.IGUIFactoryClass import IGUIFactory

class WinFactory(IGUIFactory):  
    '''
    The Concrete Win Factory Class
    '''
    def createButton(self)->IButton:       
            return WinButton()

    def createCheckbox(self)-> ICheckbox: 
            return WinCheckbox()