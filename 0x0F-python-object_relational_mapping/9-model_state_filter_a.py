#!/usr/bin/python3
"""script that lists all State objects that contain the letter 'a' from the database"""


from model_state import Base, State
import sqlalchemy
import sqlalchemy.orm
import sys


def main():
    """List the names and IDs of U.S. states in a database"""

    if len(sys.argv) < 4:
        sys.exit(1)
    engine = sqlalchemy.create_engine('mysql://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
    ))
    Base.metadata.create_all(engine)
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name.like('%a%'))
    if query.count() > 0:
        print('\n'.join(str(state.id) + ': ' + state.name for state in query))


if __name__ == '__main__':
    main()
