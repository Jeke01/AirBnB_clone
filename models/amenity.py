#!/usr/bin/python3
from models.base_model import BaseModel
"""
Dis Module is the  class: Amenity
"""


class Amenity(BaseModel):
    """our definition for Dis class Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ we will use the constructor method """
        super().__init__(self, *args, **kwargs)
