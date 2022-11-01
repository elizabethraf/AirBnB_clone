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

    def __init__(self):
        """
        Initialising a method with it's  public instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    
    def __init__(self, *args, **kwargs):
        """Base Model __init__ Method
        Here, the default values of a Base Model
        instance are initialized.
        """
        if kwargs:
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')

                if arg != '__class__':
                    setattr(self, arg, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Display Printing Method"""
        return '[{0}] ({1}) {2}'.format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update public instance"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        __dict = self.__dict__.copy()
        __dict['__class__'] = self.__class__.__name__
        __dict['created_at'] = self.created_at.isoformat()
        __dict['updated_at'] = self.updated_at.isoformat()

        return __dict
