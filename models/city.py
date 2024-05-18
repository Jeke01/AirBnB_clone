#!/usr/bin/python3
from models.base_model import BaseModel
"""
our Module class is-: City
"""


class City(BaseModel):
    """our definition for dis  class -: City"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """Usin the  constructor method """
        super().__init__(self, *args, **kwargs)
