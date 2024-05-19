#!/usr/bin/python3
"""di Module for User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Dis Class representing a User."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
