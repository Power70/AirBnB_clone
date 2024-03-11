#!/usr/bin/python3
"""
For creating the file storage instance to work with our website
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review


# dictionary of all classes
class_dict = {
        'BaseModel': BaseModel,
        'User': User,
        'City': City,
        'State': State,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review
        }
# storage, an instance of FileStorage
storage = FileStorage()
storage.reload()
