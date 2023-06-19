#!/usr/bin/python3
"""Script that lists all states in a database"""


import MySQLdb
import sys


def main():
    """Lists the names and IDs of U.S. states in a database"""

    if len(sys.argv) < 5:
        sys.exit(1)
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = connection.cursor()
    cursor.execute('''
        SELECT * FROM `states`
        WHERE BINARY `name` = %s ORDER BY `id` ASC
    ''', (sys.argv[4],))
    records = cursor.fetchall()
    if len(records) > 0:
        print('\n'.join(str(record) for record in sorted(records)))

if __name__ == '__main__':
    main()
