#!/usr/bin/python3
"""script that prints the 'State' object with the 'name' passed as argument from the database"""


from model_state import Base, State
import sqlalchemy
import sqlalchemy.orm
import sys


def main():
    """List the names and IDs of U.S. states in a database"""

    if len(sys.argv) < 5:
        sys.exit(1)
    engine = sqlalchemy.create_engine('mysql://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    ))
    Base.metadata.create_all(engine)
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    record = session.query(State).filter(State.name == sys.argv[4]).first()
    if record is None:
        print('Not found')
    else:
        print(record.id)


if __name__ == '__main__':
    main()
