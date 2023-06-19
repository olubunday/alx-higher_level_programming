#!/usr/bin/python3
"""Script that takes the name of state and lists the cities of the state in a database"""


import sys
import MySQLdb


def main(username, password, database, state_name):
    """ Connect to the MySQL server"""
    try:
        connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        return

    """Create a cursor object to execute SQL queries"""
    cursor = connection.cursor()

    try:
        """Execute the query to retrieve cities of the specified state"""
        query = f"""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = '{state_name}'
        ORDER BY cities.id ASC
        """
        cursor.execute(query)

        """Fetch all the rows from the result set"""
        rows = cursor.fetchall()

        """Print the cities"""
        for row in rows:
            city_id, city_name, state_name = row
            print(f"City ID: {city_id}, City Name: {city_name}, State: {state_name}")

    except MySQLdb.Error as e:
        print("Error executing query:", e)

    """Close the cursor and connection"""
    cursor.close()
    connection.close()

if __name__ == "__main__":
    """Check if all the required arguments are provided"""
    if len(sys.argv) != 5:
        print("Usage: python script.py [username] [password] [database] [state_name]")
    else:
        """Extract the command-line arguments"""
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        """Call the function to retrieve and print cities by state"""
        main(username, password, database, state_name)

