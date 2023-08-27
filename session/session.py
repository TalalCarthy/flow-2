import os

# DataSource
from session.datasource import load_data_sources
from session.datasource import save_data_sources

# Library
from session.library import load_libraries
from session.library import save_libraries


def initialise_data_sources(json_file_path):
    if os.path.exists(json_file_path):
        return load_data_sources(json_file_path)
    else:
        return []


def initialise_libraries(json_file_path):
    if os.path.exists(json_file_path):
        return load_libraries(json_file_path)
    else:
        return []


__all__ = ['initialise_data_sources', 'initialise_libraries',
           'save_data_sources', 'save_libraries']
