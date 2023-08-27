
import streamlit as st
import langchain
from langchain.chains import FlareChain


def set_qa():
    langchain.verbose = True
    st.session_state['qa'] = FlareChain.from_llm(
        st.session_state['llm'],
        retriever=st.session_state['library'].loadData(),
        max_generation_len=164,
        min_prob=0.3,
        verbose=True
    )


__all__ = ['set_qa']
