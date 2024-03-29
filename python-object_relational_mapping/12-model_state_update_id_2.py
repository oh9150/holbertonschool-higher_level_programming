#!/usr/bin/python3
"""
Inserts a new state "Louisiana" into the States table
"""
import sys
from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    upd_state = session.query(State).filter(State.id == 2).first()
    upd_state.name = "New Mexico"
    session.commit()
