from IDocumentClass import Document

class PDFDocument(Document):
    def __init__(self):
        self.__name = "PDF"

    def create(self):
        return f"{self.__name} document has been created."