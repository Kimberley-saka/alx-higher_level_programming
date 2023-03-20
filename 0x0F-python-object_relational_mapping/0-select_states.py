#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db_connect = MySQLdb.connect(
        username=argv[1], port=3306, password=argv[2], database=argv[3])

    cursor = db_connect.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows_selected = cursor.fetchall()

    for row in rows_selected:
        print(row)
