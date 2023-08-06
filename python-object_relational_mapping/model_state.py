#!/usr/bin/pythn3
"""
Defines a class State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Represents a state"""
    __tablename__ = "state"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
