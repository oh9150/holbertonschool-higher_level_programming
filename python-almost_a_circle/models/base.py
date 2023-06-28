#!/usr/bin/python3
"""Define a class Base"""


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
