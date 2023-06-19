#!/usr/bin/python3
"""Script that lists all cities in a database"""


import MySQLdb
import sys


def main():
    """Lists the names and IDs of U.S. states in a database"""

    if len(sys.argv) < 4:
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
        SELECT `cities`.`id`, `cities`.`name`, `states`.`name` FROM `cities`
        INNER JOIN `states` ON `cities`.`state_id` = `states`.`id`
        ORDER BY `cities`.`id`
    ''')
    records = cursor.fetchall()
    if len(records) > 0:
        print('\n'.join(str(record) for record in records))


if __name__ == '__main__':
    main()
