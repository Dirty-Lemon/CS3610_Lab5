from abc import ABC, abstractmethod

'''The GUI Interface (Product)'''

class IGUIFactory(ABC):

    @staticmethod
    @abstractmethod    
    def createButton()-> None: #static interface method      
        pass
    
    @staticmethod
    @abstractmethod
    def createCheckbox()-> None:
        pass