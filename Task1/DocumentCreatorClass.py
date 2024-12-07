from WordDocumentCreatorClass import WordDocumentCreator
from PDFDocumentCreatorClass import PDFDocumentCreator
from PPTCreatorClass import PPTDocumentCreator

class DocumentCreator():
    
    def create_document(self, objType: str):
        try:
            if (objType.lower() == 'word'): # return
                print(WordDocumentCreator().create())
                return None
            
            elif (objType.lower() == 'pdf'): # return
                print(PDFDocumentCreator().create())
                return None
            
            #ppt is powerpoint
            elif (objType.lower() == 'ppt' ): # return
                print(PPTDocumentCreator().create())
                return None
            
            else: raise Exception("Document could not be created.\n")

        except Exception as _e:
            print(_e)

        return None