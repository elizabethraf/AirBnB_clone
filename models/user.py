#!/usr/bin/python3
"""
Define a Class for User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Representation of a class for user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
