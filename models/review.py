#!/usr/bin/python3
"""Dis Module for Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Dis Class representing a Review."""
    place_id = ""
    user_id = ""
    text = ""
