from abc import ABC, abstractmethod
class Document(ABC):

    @staticmethod
    @abstractmethod
    def create()-> None:    # "-> None means function returns"
        pass