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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string, if the string is empty,
        returns an empty list"""
        if json_string = "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance of the current class with all attributes
        already set
        Args:
            dictionary (dict): The attributes
        Returns:
            The new instance
        """
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        else cls.__name__ == "Square":
            new_obj = cls(1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def save_to_file(cls, list_objs):
        """Converts all the objects in @list_objs to a dictionary using the
        @to_dictionary function, then writes the json representation of that
        list into a file named <class name>.json
        Args:
            list_objs: A list of objects of type @Rectangle or @Square
        """
        with open(cls.__name__ + ".json", "w") as f:
            list_dicts = list(map(lambda x: x.to_dictionary(), list_objs))
            f.write(Base.to_json_string(list_dicts))
