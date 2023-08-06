#!/usr/bin/python3
"""
Lists all states with their name starting with "N"
Usage: ./2-my_filter_states.py <mysql user> <mysql password> <db> <state>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    for state in cur.fetchall():
        if state[1] == sys.argv[4]:
            print(state)
    cur.close()
    db.close()
