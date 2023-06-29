#!/usr/bin/python3
"""Defines a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates a square
        Args:
            size (int): The size of the square
            x (int): The x position of the square
            y (int): The y position of the square
            id (int): The identifier of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
