#!/usr/bin/python3
import os.path
import json
import os
"""
Module file_storage
Contains the FileStorage class
responsible for serializing instances to a JSON file and
deserializing JSON file to instances
"""


class FileStorage():
    """
    Handles serialization of instances to a JSON file and deserialization of JSON file to instances
    """
    ''' Initialize file path and objects dictionary '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Return the dictionary of all objects '''
        return self.__objects

    def new(self, obj):
        ''' Add a new object to the __objects dictionary with key <obj class name>.id '''
        if obj:
            ''' Add the object and its key to __objects if the object is not None '''
            name = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[name] = obj

    def save(self):
        ''' Serialize __objects to the JSON file specified by __file_path '''
        my_dict = {}

        for keys, val in self.__objects.items():
            ''' Serialize each object with its key '''
            my_dict[keys] = val.to_dict()

        with open(self.__file_path, "w") as my_file:
            json.dump(my_dict, my_file)

    def reload(self):
        ''' Deserialize the JSON file to __objects '''

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        my_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r") as file_path:
            objects = json.load(file_path)
            self.__objects = {}
            for key in objects:
                name = key.split(".")[0]
                self.__objects[key] = my_dict[name](**objects[key])

