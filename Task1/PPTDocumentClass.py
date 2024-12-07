from IDocumentClass import Document

class PPTDocument(Document):
    def __init__(self):
        self.__name = "PPT"
    def create(self):
        return f"{self.__name} document has been created."