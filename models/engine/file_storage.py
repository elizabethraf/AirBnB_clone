#!/usr/bin/python3
"""
Display FileStorage that serializes instances to a JSON file and deserializes
JSON file to instances.
"""
import json
from os import path
from models.user import User


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
            self.__objects["{}.{}".format(str(type(obj).__name__), obj.
                                          id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        self.__objects = __file_path()
        dict_temp = {}
        for key, value in FileStorage.__objects.items():
            dict_prev[key] = value.to_dict()
            with open(FileStorage.__file_path, "w") as f:
                f.write(json.dumps(dict_prev))

    def reload(self):
        """deserializes the JSON file to __objects"""
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r',
                      encoding='utf-8') as f:
                try:
                    json_dict = json.loads(f.read())
                except Exception as e:
                    print("problem while loading a file with error: {}".\
                            format(e))
                    json_dict = {}
                for a, b in json_dict.items():
                    FileStorage.__objects[a] = eval(b['__class__'])(**b)
