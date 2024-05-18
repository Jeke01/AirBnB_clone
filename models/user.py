#!/usr/bin/python3
"""this is our code for the user class
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''Dis is fr the base model class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
