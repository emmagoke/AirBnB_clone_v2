#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """Initializes the City instance """
        super().__init__(*args, **kwargs)

    if models.db_type != 'db':
        from models.city import City

        @property
        def cities(self):
            """ A getter method for all City related to the current State """
            state_city = []
            all_cities = models.storage.all(City)

            for city in all_cities:
                if self.id == city.state_id:
                    state_city.append(city)
            return state_city
