#!/usr/bin/python3
"""
Define a Class for User"""

from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """Representation of a class for user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
