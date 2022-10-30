#!/usr/bin/python3
"""
Display FileStorage that serializes instances to a JSON file and deserializes
JSON file to instances.
"""

from models.engine.file_storage import FileStorage
import json
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    serialisation instances to a JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary objects"""
        return (self.__objects)

    def new(self, obj):
        """Display objects in sets"""
        if obj:
            self._objects["{}".format(str(type(obj).__name__), obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        self.__objects = __file_path()

    def reload(self):
        """deserializes the JSON file to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.loads(f.read())
                for k, v in json_dict.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
