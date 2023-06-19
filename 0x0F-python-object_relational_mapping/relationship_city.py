#!/usr/bin/python3
"""Module that improves model_city.py file"""


from relationship_state import Base, State
import sqlalchemy
import sqlalchemy.orm


class City (Base):
    """A U.S. city stored in a database

    Attributes:
        id (int): a unique ID for this record
        name (str): name of the state
        state (State): state this city is in
        state_id (int): the ID of the state in which this state resides

    """

    __tablename__ = 'cities'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(256), nullable=False)
    state_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('states.id')
    )
