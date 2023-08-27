import streamlit as st

from session.session import initialise_libraries
from session.session import initialise_data_sources
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory


def reset():
    if 'data-sources' not in st.session_state:
        st.session_state['data-sources'] = initialise_data_sources(
            './session/data-sources.json')
    if 'libraries' not in st.session_state:
        st.session_state['libraries'] = initialise_libraries(
            './session/libraries.json')
    if 'llm' not in st.session_state:
        st.session_state['llm'] = ChatOpenAI(
            temperature=0, streaming=True)
    if 'memory' not in st.session_state:
        st.session_state['memory'] = ConversationBufferMemory(
            memory_key="chat_history")
    if 'max_tokens' not in st.session_state:
        st.session_state['max_tokens'] = 4096
    if 'chat-mode' not in st.session_state:
        st.session_state['chat-mode'] = 'set-config'


__all__ = ['reset']
