#!/usr/bin/python3
"""This module contains the FileStorage class
which handles the serialization and deserialization
of the instances of BaseModel class in using json format
for the project"""

import json
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place


class FileStorage():
    """The class for handling file storage

    It handles the serilization of the instances to JSON file
    and the deserialization of the JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """returns the class attribure __objects

        Returns:
            dict: the dictionary that stores all objects
        """

        return FileStorage.__objects

    def new(self, obj) -> None:
        """For adding new object instances

        Args:
            obj: the object to store
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self) -> None:
        """To save all the object in the class to a json file

        Serialize all the object to a JSON file
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as fd:
            json.dump(objdict, fd)

    def reload(self) -> None:
        """To deserialized the JSON file

        deserialized the JSON file to __objects if the __file_path
        exist else do nothing and no exception should be raised
        """
        try:
            with open(FileStorage.__file_path) as fd:
                objdict = json.load(fd)
            for key, value in objdict.items():
                cls_name = value["__class__"]
                del value["__class__"]
                if cls_name in models.class_dict:
                    cls_name_found = models.class_dict[cls_name]
                    self.__objects[key] = cls_name_found(**value)
        except FileNotFoundError:
            pass

    # custom helper methods

    @property
    def file_path(self):
        return self.__file_path

    @property
    def objects(self):
        return self.__objects
