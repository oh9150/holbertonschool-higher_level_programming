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

    def update(self, *args, **kwargs):
        """Updates the square's attributes
        Args:
            args (ints): The new parameters
                1. The new id for the square
                2. The new size for the square
                3. The new x position for the square
                4. The new y position for the square
        """
        if args and len(args) > 0:
            arg_count = 0
            for arg in args:
                if arg_count == 0:
                    self.id = arg
                elif arg_count == 1:
                    self.width = arg
                    self.height = arg
                elif arg_count == 2:
                    self.x = arg
                elif arg_count == 3:
                    self.y = arg
                arg_count += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of the square"""
        return {"id": self.id,
                "x": self.x,
                "size": self.width
                "y": self.y
                }

    @property
    def size(self):
        """Getter for the size property"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size property"""
        self.width = value
        self.height = value
