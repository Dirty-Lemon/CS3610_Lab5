from AbstractFactoryA2.ICheckboxClass import ICheckbox

class WinCheckbox(ICheckbox):
    
    def __init__(self):
        self.__height = 6
        self.__width = 6
        self.__color = 'blue'
        
    def get_checkbox(self):
        return{
            "Description":"I am a blue window Checkbox ",
            "width": self.__width,
            "height": self.__height,
            "color": self.__color
        }