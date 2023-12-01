#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, Table
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from models.place import Place, place_amenity
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
