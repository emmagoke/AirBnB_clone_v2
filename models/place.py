#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    #  city_id = ""
    #  user_id = ""
    #  name = ""
    #  description = ""
    #  number_rooms = 0
    #  number_bathrooms = 0
    #  max_guest = 0
    #  price_by_night = 0
    #  latitude = 0.0
    #  longitude = 0.0
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', cascade='all, delete',
                               backref='place')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        import models
        from models.review import Review

        @property
        def reviews(self):
            """
            This is a getter attribute that returns the list of
            Review instances with place_id equals to the current Place.id
            """
            place_review = []
            all_reviews = models.storage.all(Review)

            for review in all_reviews:
                if self.id == review.place_id:
                    place_review.append(review)
            return place_review
