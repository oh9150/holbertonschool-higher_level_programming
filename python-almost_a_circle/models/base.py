#!/usr/bin/python3
"""Define a class Base"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiates a Base class
        Args:
            id (int): The id for the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts @list_dictionaries to a JSON string
        Args:
            The string to convert
        Returns:
            The converted string
        """
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        return json.dumps(list_dictionaries)
