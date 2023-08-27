import os

from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import LLMChain, HypotheticalDocumentEmbedder
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader


os.environ['OPENAI_API_KEY'] = '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'

doc = None
# with open("../files/file.txt") as f:
#     doc = f.read()
doc = PyPDFLoader("./file-1.pdf").load()
text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
texts = text_splitter.split_text(doc[0].page_content)


base_embeddings = OpenAIEmbeddings()
llm = OpenAI()
prompt_template = """Please answer the user's questions
Question: {question}
Answer in german:"""
prompt = PromptTemplate(input_variables=["question"], template=prompt_template)
llm_chain = LLMChain(llm=llm, prompt=prompt)

embeddings = HypotheticalDocumentEmbedder(
    llm_chain=llm_chain, base_embeddings=base_embeddings
)

docsearch = Chroma.from_texts(texts, embeddings)

query = "What did Elad Rave do?"
docs = docsearch.similarity_search(query)

print(docs[0].page_content)
