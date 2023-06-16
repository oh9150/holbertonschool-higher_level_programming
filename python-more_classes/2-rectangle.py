#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Returns the current width
        Returns:
            The current width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width to value
        Args:
            value (int): The value to set the width to
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the current height
        Returns:
            The current height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height to @value
        Args:
            value (int): The value to set the height to
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle
        Returns:
            The area of the rectange
        """
        return self.height * self.width

    def perimeter(self):
        """Returns the perimeter of the rectangle
        Returns:
            The perimeter of the rectangle
        """
        return (self.height * 2) + (self.width * 2)
