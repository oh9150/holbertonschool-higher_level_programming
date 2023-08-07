#!/usr/bin/python3
"""
Defines a class State
"""
from sqlalchemy import Column, Integer, Stringi, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(metadata=MetaData())

class State(Base):
    """
    Represents a state
    """
    __tablename__ = "state"
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
