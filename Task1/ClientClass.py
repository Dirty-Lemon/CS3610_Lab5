from DocumentCreatorClass import DocumentCreator

# class Client:
def get_doc_type()-> str:
    print('What type of document would you like to create?')
    docType = input()
    documentCreator = DocumentCreator()
    return documentCreator.create_document(docType)

#client can enter "word", "ppt", or "pdf" (capitalization doesn't matter) to get a document
get_doc_type()