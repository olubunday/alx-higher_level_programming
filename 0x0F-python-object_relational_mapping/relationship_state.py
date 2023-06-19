#!/usr/bin/python3
"""Module that improves the model_state.py file"""


import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm


Base = sqlalchemy.ext.declarative.declarative_base()


class State (Base):
    """A U.S. state stored in a database

    Attributes:
        cities (List[City]): list of cities in this state
        id (int): a unique ID for this record
        name (str): name of the state

    """

    __tablename__ = 'states'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(256), nullable=False)
    cities = sqlalchemy.orm.relationship(
        'City',
        backref='state',
        cascade='all, delete-orphan'
    )
