#!/usr/bin/bash
from models.base_model import BaseModel

"""The city class which represent the class for Cities in the program"""


class City(BaseModel):
    """The city class which is for making cities objects"""

    state_id = ""
    name = ""
