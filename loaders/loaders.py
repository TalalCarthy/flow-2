
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import Docx2txtLoader


def getLoader(filePath):
    if filePath.lower().endswith('.txt'):
        return TextLoader(filePath, encoding="utf-8")
    elif filePath.lower().endswith('.pdf'):
        return PyPDFLoader(filePath)
    elif filePath.lower().endswith('.docx'):
        return Docx2txtLoader(filePath)
    else:
        return None
