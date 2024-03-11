#!/usr/bin/python3
from models.base_model import BaseModel
"""The class for reviews"""


class Review(BaseModel):
    """The review class"""

    place_id = ""
    user_id = ""
    text = ""
