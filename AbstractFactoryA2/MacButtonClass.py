from AbstractFactoryA2.IButtonClass import IButton
'''
The MacButton Concrete Class implements the IButton & IMac interface
'''
class MacButton(IButton):  
    def __init__(self):
        self.__height = 3
        self.__width = 5
        self.__color = 'red'

    def get_button(self):
        return {
            'Description' : 'I am a red mac Button', 
            "width": self.__width,
            "height": self.__height,
            "color": self.__color
        }

