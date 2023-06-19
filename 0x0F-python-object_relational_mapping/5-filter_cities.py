#!/usr/bin/python3
"""Module to list states in a database"""


import MySQLdb
import sys


def main():
    """List the names and IDs of U.S. states in a database"""

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
        SELECT `cities`.`name` FROM `cities`
        INNER JOIN `states` ON `cities`.`state_id` = `states`.`id`
        WHERE `states`.`name` = %s
        ORDER BY `cities`.`id`
    ''', (sys.argv[4],))
    records = cursor.fetchall()
    print(', '.join(record[0] for record in records))


if __name__ == '__main__':
    main()
