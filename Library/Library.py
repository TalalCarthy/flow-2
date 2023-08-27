from DataSource import DataSource
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema.document import Document

# Library


class Library:
    def __init__(self, name: str, sources=[]):
        self.sources = sources
        self.name = name

    def __str__(self):
        return self.name

    def loadData(self):
        documents = []
        for source in self.sources:
            prefix = Document(page_content="source name: " + source.name + " file name: " + source.path +
                              ":\n=====================================================\n")
            prefix.metadata = {'source': source.path, 'page': 0}

            postfix = Document(
                page_content="\n=====================================================\n")
            postfix.metadata = {'source': source.path}

            documents.extend([prefix] + source.load() + [postfix])
        text_splitter = CharacterTextSplitter(chunk_size=2048, chunk_overlap=0)
        documents = text_splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(documents, embeddings)
        return vectorstore.as_retriever()


__all__ = ['Library']
