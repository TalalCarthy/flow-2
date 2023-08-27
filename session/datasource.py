
import streamlit as st
import json
from DataSource.DataSource import DataSource

# Gets DataSources from file
# @param json_file_path - path to json file


def load_data_sources(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    data_sources = []
    for item in data:
        name = item.get('name')
        path = item.get('path')
        if name and path:
            data_source = DataSource(name, path)
            data_sources.append(data_source)

    return data_sources

# Saves DataSources to file
# @param json_file_path - path to json file
# @param sources - array of DataSources to save


def save_data_sources(sources, json_file_path):
    data = []
    for data_source in sources:
        data.append({
            'name': data_source.name,
            'path': data_source.path
        })

    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)


__all__ = ['load_data_sources', 'save_data_sources']
