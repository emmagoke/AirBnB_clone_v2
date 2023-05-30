#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade="all, delete")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the State instance """
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        #  from models.city import City

        @property
        def cities(self):
            """ A getter method for all City related to the current State """
            from models.city import City

            state_city = []
            print(City)
            all_cities = models.storage.all(City)

            for city in all_cities.values():
                if self.id == city.state_id:
                    state_city.append(city)
            return state_city
