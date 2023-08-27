import streamlit as st

from DataSource.DataSource import DataSource

from duplicators.duplicators import save_file
from session.session import save_data_sources
from reset.reset import reset
from reset.deleteFilesInFolder import deleteFilesInFolder


# initialise session and load the libraries and data sources
reset()

st.title("DataSource")
st.write("DataSource management")

with st.form("Create a DataSource", clear_on_submit=True):
    name = st.text_input('Please write DataSource name')

    uploaded_file = st.file_uploader(
        "Upload a file:", type=['txt', 'pdf', 'docx'])

    if uploaded_file is not None:
        file_path = f'./files/{uploaded_file.name}'
        save_file(uploaded_file, file_path)

    submitted = st.form_submit_button("Create DataSource")
    if submitted:
        source = DataSource(name, file_path)
        st.session_state['data-sources'].append(source)
        save_data_sources(
            st.session_state['data-sources'], './session/data-sources.json')
        st.success('DataSource creates successfully')

deleteAllFiles = st.button("Clear Files directory")
if deleteAllFiles:
    deleteFilesInFolder('./files')
    st.session_state['data-sources'] = []
    st.session_state['libraries'] = []


st.subheader("DataSources:")
for index, data_source in enumerate(st.session_state['data-sources']):
    st.write(index, data_source.name, data_source.path)
