#!/usr/bin/python3
"""This is the state class"""
import models
from models.city import City
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import Base
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", backref="state", cascade="delete")
    else:
        name = ""
        @property
        def cities(self):
            """ Getter attribute """
            cs = []
            for city in models.storage.all(City).values():
                if (city.state_id == self.id):
                    cs.append(city)
            return cs
