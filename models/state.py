#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete")
    else:
        @property
        def cities(self):
            """Returns the list of City instances
            with state_id equals to the current State.id"""
            from models import storage
            all_cities = storage.all(City)
            return [city for city in all_cities.values() if city.state_id == self.id]
