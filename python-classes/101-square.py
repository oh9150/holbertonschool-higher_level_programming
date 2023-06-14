#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square
        Args:
            size (int): The size of the square
        """
        self.size = size
        self.position = position

    def area(self):
        """Returns the current square area
        Returns:
            The current area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Gets the size of the square
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square
        Args:
            value (int): The size to set the square
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """Returns the position of a square
        Returns:
            The current position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square
        Args:
            value (int): The position of the square
        """
        if (isinstance(value, tuple)
                and len(value) == 2
                and isinstance(value[0], int)
                and isinstance(value[1], int)
                and value[0] >= 0
                and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Prints the square"""
        for ypos in range(self.position[1]):
            print("")
        for height in range(self.size):
            for xpos in range(self.position[0]):
                print(" ", end="")
            for width in range(self.size):
                print("#", end="")
            print("")
        if self.size == 0:
            print("")

    def __str__(self):
        """Returns a string to print"""
        retstr = ""
        for ypos in range(self.position[1]):
            retstr += "\n"
        for height in range(self.size):
            for xpos in range(self.position[0]):
                retstr += " "
            for width in range(self.size):
                retstr += "#"
            retstr += "\n"
        if self.size == 0:
            retstr += "\n"
        return retstr
