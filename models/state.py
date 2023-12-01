#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv
from models.city import City
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            all_cities = storage.all(City).values()
            return [city for city in all_cities if city.state_id == self.id]
