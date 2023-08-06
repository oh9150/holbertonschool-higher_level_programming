#!/usr/bin/python3
"""
Lists all cities from the database hbtn_03_4_usa
Usage: ./4-cities_by_state.py <mysql user> <mysql pass> <db>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
               FROM cities \
               INNER JOIN states ON cities.state_id = states.id \
               ORDER BY cities.id ASC")
    for city in cur.fetchall():
        print(city)
