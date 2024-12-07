from PPTDocumentClass import PPTDocument
from IDocumentClass import Document

class PPTDocumentCreator:

    def create(self)-> Document:
        return PPTDocument().create()