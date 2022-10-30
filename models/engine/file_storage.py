#!/usr/bin/python3
"""
Display FileStorage that serializes instances to a JSON file and deserializes
JSON file to instances.
"""
import json
from os import path


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
            self.__objects["{}.{}".format(str(type(obj).__name__), obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        self.__objects = __file_path()

    def reload(self):
        """deserializes the JSON file to __objects"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.loads(f.read())
                for a, b in json_dict.items():
                    self.__objects[a] = eval(b['__class__'])(**b)
