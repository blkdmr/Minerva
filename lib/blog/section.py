from sqlalchemy import create_engine, ForeignKey, Column, String
from lib.utils.data.base import Base

class Section(Base):

    __tablename__ = "sections"
    _title = Column("title", String)
    _path = Column("path", String, primary_key=True)

    def __repr__(self):
        return f"Debug: Title {self._title}. {self._path}\n"
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value:str):
        self._title = value

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value:str):
        self._path = value