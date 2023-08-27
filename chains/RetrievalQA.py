from langchain.chains import RetrievalQA
import streamlit as st


def set_qa():
    st.session_state['qa'] = RetrievalQA.from_chain_type(
        llm=st.session_state['llm'],
        chain_type=st.session_state['document_type'],
        retriever=st.session_state['library'].loadData(),
        verbose=True)


__all__ = ['set_qa']
