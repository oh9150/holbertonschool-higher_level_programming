#!/usr/bin/python3
"""
Defines a class State and an object Base that's an instance of declarative_base
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """
    Represents a state
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
