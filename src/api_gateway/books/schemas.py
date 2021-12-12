"""
Classes for viewing information about books
"""
import datetime

from pydantic import BaseModel


class BookMeta(BaseModel):
    """Data, which contains main information about book"""
    title: str
    author: str

    class Config:
        """Configuration of pydantic model"""
        # read the data even if it is not a dict, but an ORM model
        # (or any other arbitrary object with attributes).
        orm_mode = True


class BookProfile(BaseModel):
    """Data, which contains whole information about book (except for content)"""
    title: str
    author: str
    publication_date: datetime.date
    description: str

    class Config:
        """Configuration of pydantic model"""
        # read the data even if it is not a dict, but an ORM model
        # (or any other arbitrary object with attributes).
        orm_mode = True
