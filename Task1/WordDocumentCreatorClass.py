from WordDocumentClass import WordDocument
from IDocumentClass import Document

class WordDocumentCreator:

    def create(self)-> Document:
        return WordDocument().create()