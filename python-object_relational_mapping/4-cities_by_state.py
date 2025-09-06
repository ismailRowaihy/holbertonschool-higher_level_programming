#!/usr/bin/python3
"""this Module is a python script
that sends a query and prints it"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT c.id,c.name,s.name FROM cities c \
         INNER JOIN states s ON c.state_id = s.id \
         ORDER BY c.id ASC"
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
