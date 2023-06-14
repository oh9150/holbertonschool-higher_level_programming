#!/usr/bin/python3
"""Defines a class Square"""
class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes the square
        Args:
            size (int): The size of the square
        """
        self.size(size)

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
