#!/usr/bin/python3
"""
Safe from SQL injections
"""
import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s \
                   ORDER BY states.id ASC", {'name': sys.argv[4]})
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
