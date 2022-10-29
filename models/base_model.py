#!/usr/bin/python3
"""
Define BaseModel

"""

import uuid
import json
from datetime import datetime


class BaseModel:
    """
    Base Model for the project

    """

    def __init__(self, *args, **kwargs):
        """
        Initialising a method with it's  public instance attributes
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Display Printing Method"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Update the public instance"""
        self.update_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""

        __dict = self.__dict__.copy()
        __dict["__class__"] = type(self).__name__
        __dict["created_at"] = self.created_at.isoformat()
        __dict["updated_at"] = self.updated_at.isoformat()

        return __dict
