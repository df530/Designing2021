"""
Books database submodule
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()


class BooksDatabase:
    """Class containing some objects for working with databases"""
    def __init__(self, postgresql_database_url):
        """
        :param postgresql_database_url:

        Creates database if it doesn't exist
        """
        self.engine = create_engine(postgresql_database_url)
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
