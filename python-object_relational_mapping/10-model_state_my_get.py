#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
Usage: ./7-model_state_fetch_all <mysql user> <mysql passwd> <db> <state name>
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

    states = session.query(State).order_by(State.id).all()
    found = False
    for state in states:
        if state.name == sys.arggv[4]:
            print("{}: {}".format(state.id, state.name))
            found = True
            break

    if found == False:
        print("Not found")
