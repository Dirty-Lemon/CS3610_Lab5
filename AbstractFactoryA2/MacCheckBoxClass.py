from AbstractFactoryA2.ICheckboxClass import ICheckbox

class MacCheckbox(ICheckbox):
    def __init__(self):
        self.__height = 4
        self.__width = 4
        self.__color = 'red'

    def get_checkbox(self):
        return {
            "Description":"I am a red mac Checkbox ",
            "width": self.__width,
            "height": self.__height,
            "color": self.__color
        }
