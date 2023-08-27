import streamlit as st

from reset.reset import reset
from Library.Library import Library

from session.session import save_libraries

# initialise session and load the libraries and data sources
reset()

with st.form("Create a Library", clear_on_submit=True):
    name = st.text_input('Please write Library name:')
    sources = []

    st.write("Add DataSources:")
    for source in st.session_state['data-sources']:
        if st.checkbox(label=source.name):
            sources.append(source)

    submitted = st.form_submit_button("Create Library")
    if submitted:
        library = Library(name, sources)
        st.session_state['libraries'].append(library)
        save_libraries(
            st.session_state['libraries'], './session/libraries.json')

st.subheader("Libraries:")
for index, library in enumerate(st.session_state['libraries']):
    st.write(index, library.name)
