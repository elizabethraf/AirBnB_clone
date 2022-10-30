#!/usr/bin/python3
"""
Define FileStorage, FileStorage` class is loaded with all objects on the
`__file_path` class attribute of the `FileStorage` class.

"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage  import FileStorage

storage = FileStorage()
storage.reload()
