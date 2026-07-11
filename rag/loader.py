from langchain_community.document_loaders import Docx2txtLoader

class DocumentLoader:
    def __init__(self, path):
        self.path = path

    def load(self):
        loader = Docx2txtLoader(self.path)
        return loader.load()
    

