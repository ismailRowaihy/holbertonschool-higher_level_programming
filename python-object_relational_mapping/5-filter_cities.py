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
        "SELECT c.name FROM cities c \
         INNER JOIN states s ON c.state_id = s.id \
         WHERE BINARY s.name = %s\
         ORDER BY c.id ASC", (sys.argv[4],)
    )
    query_rows = cur.fetchall()
    print(', '.join([i[0] for i in query_rows]))
    cur.close()
    conn.close()
