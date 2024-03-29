#!/usr/bin/python3
"""
Lists all states with their name starting with "N"
Usage: ./1-filter_states <mysql user> <mysql password> <database>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    for state in cur.fetchall():
        if state[1][0] == "N":
            print(state)
    cur.close()
    db.close()
