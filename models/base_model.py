#!usr/bin/python3
""" BaseModel class module"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """Class that defines all common attibutes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initializes instances of the class with
        id, created_at and updated_at attributes when created
        Args:
            args (list/tuple): for any number of positional arguments
            kwargs (dict): for any number of keyword arguments
        Attrs:
            id (str): unique identifier for instances of the class
            created_at (datetime): the current datetime when an instance
                is created
            updated_at (datetime): the current datetime when an instance is
            created and when changes are made to it
        """
        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                        )
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            current_time = datetime.now()
            self.created_at = current_time
            self.updated_at = current_time
            models.storage.new(self)

    def __str__(self):
        """Defines the string representation of the class instance"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """Updates the `updated_at` public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__
        of the instance"""
        data_dict = {
                key: value for key, value in self.__dict__.items()
                if value is not None
            }
        data_dict["__class__"] = self.__class__.__name__

        # datetime attrs are converted to string object in ISO format
        data_dict["created_at"] = str(self.created_at.isoformat())
        data_dict["updated_at"] = str(self.updated_at.isoformat())

        return data_dict
