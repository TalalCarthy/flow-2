from langchain.chains import ConversationalRetrievalChain
import streamlit as st


def set_qa():
    st.session_state['qa'] = ConversationalRetrievalChain.from_llm(
        st.session_state['llm'],
        st.session_state['library'].loadData(),
        memory=st.session_state['memory'],
        verbose=True)


__all__ = ['set_qa']
