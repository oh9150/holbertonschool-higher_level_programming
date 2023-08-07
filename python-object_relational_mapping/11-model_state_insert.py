#!/usr/bin/python3
"""
Inserts a new state "Louisiana" into the States table
"""
import sys
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State("Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)
