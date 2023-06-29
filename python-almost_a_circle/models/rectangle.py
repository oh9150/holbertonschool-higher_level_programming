#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates a rectangle
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): The x position of the rectangle
            y (int): The y position of the rectangle
            id (int): The id of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """Returns the area of the rectangle
        Returns:
            The area of the rectangle
        """
        return self.height * self.width

    def display(self):
        """Prints in stdout the instance with the character '#'"""
        for y in range(self.y):
            print("")
        for row in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for col in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """Returns the string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args):
        arg_count = 0
        for arg in args:
            if arg_count == 0:
                self.id = arg
            elif arg_count == 1:
                self.width = arg
            elif arg_count == 2:
                self.height = arg
            elif arg_count == 3:
                self.x = arg
            elif arg_count == 4:
                self.y = arg

    @property
    def width(self):
        """Getter for the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width property"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height property"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x property"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y property"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must >= 0")
        self.__y = value
