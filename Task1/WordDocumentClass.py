from IDocumentClass import Document

class WordDocument(Document):
    def __init__(self):
        self.__name = "Word"
    def create(self):
        return f"{self.__name} document has been created."