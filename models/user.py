#!/usr/bin/python3
from models.base_model import BaseModel
"""The user class that inherit from the BaseModel

The user class represents the User of the AirBnB
"""


class User(BaseModel):
    """User class which inherit from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
