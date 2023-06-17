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
            The perimeter of the rectangle, or if height or width == 0, 0
        """
        if self.width > 0 and self.height > 0:
            return (self.height * 2) + (self.width * 2)
        return 0

    def __str__(self):
        """Returns the string to print using print() or str()
        Returns:
            The string to print
        """
        retstr = ""
        if self.height > 0 and self.width > 0:
            return retstr
        for height in range(self.height):
            for width in range(self.width):
                retstr += "#"
            retstr += "\n"
        return retstr

    def __repr__(self):
        """Returns the repr() representation of the object
        Returns:
            The repr() representation of the object
        """
        return "Rectangle({}, {})".format(self.width, self.height)

