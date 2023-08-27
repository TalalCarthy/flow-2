import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import SimpleSequentialChain
from langchain.callbacks import StreamlitCallbackHandler

from planner.planner import planner_template as planner_default
from planner.planner import create_planner

from reset.reset import reset
from chains.RetrievalQA import set_qa as retrieval_qa
from chains.FLARE import set_qa as flare
from chains.ConversationalRetrievalQA import set_qa as conversational_retrieval_qa
# Import things that are needed generically

# initialise session and load the libraries and data sources
reset()


library_names = [library.name for library in st.session_state['libraries']]


with st.sidebar:
    selected_library_name = st.selectbox("Select a Library", library_names)
    document_type = st.selectbox(
        'Select document type', ('stuff', 'refine', 'map_reduce', 'map_rerank')
    )
    chain_type = st.selectbox(
        'Select chain type', ("FLARE", "HyDE",
                              "ConversationalRetrievalQA", "Retrieval QA")
    )
    selected_library = None

    for library in st.session_state['libraries']:
        if library.name == selected_library_name:
            selected_library = library
            break
    max_tokens = st.number_input("Max Tokens:", min_value=0, value=4096)
    use_planner = st.checkbox("Use Planner?")
    planner_template = st.text_area(
        "Planner Template:", value=planner_default)

    set_config = st.button('Set Configuration')
    if set_config:
        if selected_library is not None:
            st.session_state['library'] = selected_library
        if document_type is not None:
            st.session_state['document_type'] = document_type
        if chain_type == "FLARE":
            flare()
        elif chain_type == "Retrieval QA":
            retrieval_qa()
        elif chain_type == "ConversationalRetrievalQA":
            conversational_retrieval_qa()
        st.session_state['max_tokens'] = max_tokens

        st.session_state['planner'] = create_planner(planner_template)

        llm = OpenAI(temperature=0, max_tokens=st.session_state['max_tokens'])
        model = ChatOpenAI(temperature=0, streaming=True, model="gpt-4",
                           max_tokens=st.session_state['max_tokens'])
        st.session_state['planner_chain'] = SimpleSequentialChain(
            chains=[st.session_state['planner'], st.session_state['qa']], verbose=True)
        st.session_state['planner_mode'] = use_planner
        st.session_state['chat-mode'] = 'chat'


# initialize the callback handler with a container to write to

chat_disabled = st.session_state['chat-mode'] == 'set-config'


if prompt := st.chat_input(disabled=chat_disabled):
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(
            st.container())
        if st.session_state['planner_mode']:
            executor = 'planner_chain'
        else:
            executor = 'qa'
        response = st.session_state[executor].run(
            prompt, callbacks=[st_callback])
        st.write(response)
