from abc import ABC, abstractmethod

'''The Checkbox  Interface (Product)'''

class ICheckbox(ABC):
    
    @staticmethod
    @abstractmethod
    def get_checkbox()-> None: #static interface method
        pass

