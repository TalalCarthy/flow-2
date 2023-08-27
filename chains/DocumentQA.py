import openai
import os

from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.indexes.vectorstore import VectorstoreIndexCreator

os.environ['OPENAI_API_KEY'] = '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'

raw_text = None

with open("../files/document.txt") as f:
    raw_text = f.read()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_text(raw_text)

embeddings = OpenAIEmbeddings()

docsearch = Chroma.from_texts(texts, embeddings, metadatas=[
                              {"source": str(i)} for i in range(len(texts))]).as_retriever()

prompt_template = """
    You are a helpful assistant, use the following pieces of context to answer
    the question at the end If you don't know the answer, just say that you don't know, don't try to make up an answer

    context: {context}
    Question: {question}
    Answer:
"""

question_prompt = PromptTemplate(template=prompt_template,
                                 input_variables=['context', 'question'])

combine_prompt_template = """Given the following extracted parts of a long document and a question, create a final answer. 
If you don't know the answer, just say that you don't know. Don't try to make up an answer.

QUESTION: {question}
=========
{summaries}
=========
Answer:"""
combine_prompt = PromptTemplate(
    template=combine_prompt_template, input_variables=["summaries", "question"]
)


# chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff", prompt=prompt)

# map-reduce
chain = load_qa_chain(OpenAI(temperature=0),
                      chain_type="map_reduce",
                      return_map_steps=True,
                      question_prompt=question_prompt,
                      combine_prompt=combine_prompt,
                      verbose=True)

query = "Who are the members of the nakama?"
docs = docsearch.get_relevant_documents(query)

# response = chain.run(input_documents=docs, question=query)
# print(response)

response = chain({"input_documents": docs, "question": query},
                 return_only_outputs=True)
print(response)
