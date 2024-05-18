#!/usr/bin/python3
from models.base_model import BaseModel
"""
our Module class is-: Place
"""


class Place(BaseModel):
    """our definition for Dis  class Place"""
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longtude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ usin the constructor method """
        super().__init__(self, *args, **kwargs)
