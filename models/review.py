#!/usr/bin/python3
"""
module for BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Display ttributes
    """
    place_id = ""
    user_id = ""
    text = ""
