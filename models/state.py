#!/usr/bin/python3
from models.base_model import BaseModel
"""
our Module class is-: State
"""


class State(BaseModel):
    """our definition for Dis class State"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ usin the constructor method """
        super().__init__(self, *args, **kwargs)
