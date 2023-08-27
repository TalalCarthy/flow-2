
import json
from Library.Library import Library
from DataSource.DataSource import DataSource


def load_libraries(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    libraries = []
    for item in data:
        name = item.get('name')
        sources_data = item.get('sources')
        if name and sources_data:
            sources = []
            for source_data in sources_data:
                source_name = source_data.get('name')
                source_path = source_data.get('path')
                if source_name and source_path:
                    source = DataSource(source_name, source_path)
                    sources.append(source)

            library = Library(name, sources)
            libraries.append(library)

    return libraries


def save_libraries(libraries, json_file_path):
    data = []
    for library in libraries:
        sources_data = []
        for source in library.sources:
            sources_data.append({
                'name': source.name,
                'path': source.path
            })
        data.append({
            'name': library.name,
            'sources': sources_data
        })

    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)


__all__ = ['load_libraries', 'save_libraries']
