#!/usr/bin/python3
"""
Define BaseModel
"""
import uuid


class BaseModel:
    """
    Base Model for the project
    """

    def __init__(self):
        """
        Initialising a method with it's  public instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Display Printing Method"""
        return '[{0}] ({1}) {2}'.format(
                self.__class__.__name__, self.id, self.__dict__)
