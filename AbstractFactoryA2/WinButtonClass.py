from AbstractFactoryA2.IButtonClass import IButton

class WinButton(IButton):
    
    def __init__(self):
        self.__height = 5
        self.__width = 7
        self.__color = 'blue'
        
    def get_button(self):
        return{
            'Description':"I am a blue window Button ",
            "width": self.__width,
            "height": self.__height,
            "color": self.__color
        }