
from loaders.loaders import getLoader


class DataSource:
    def __init__(self, name: str, path: str):
        self.path = path
        self.name = name

    def __str__(self):
        return self.name

    def load(self):
        return getLoader(self.path).load()


__all__ = ['DataSource']
