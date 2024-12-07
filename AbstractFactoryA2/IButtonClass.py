from abc import ABC, abstractmethod

'''The Button  Interface (Product)'''

class IButton(ABC):
    
    @staticmethod
    @abstractmethod
    def get_button()-> None: #static interface method
        #gets a button win/mac
        pass

