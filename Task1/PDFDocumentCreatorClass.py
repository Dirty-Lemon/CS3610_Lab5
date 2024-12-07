from PDFDocumentClass import PDFDocument
from IDocumentClass import Document

class PDFDocumentCreator:

    def create(self)-> Document:
        return PDFDocument().create()