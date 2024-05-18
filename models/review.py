#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
from models.user import User
"""
the Module class is-: Review
"""


class Review(BaseModel):
    """our definition for Dis class Review"""
    text = ""
    place_id = ""
    user_id = ""

    def __init__(self, *args, **kwargs):
        """ usin the constructor method """
        super().__init__(self, *args, **kwargs)
