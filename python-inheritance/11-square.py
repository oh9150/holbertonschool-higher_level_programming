#!/usr/bin/python3
Square = __import__("9-rectangle.py").Rectangle


"""Defines a class Square"""
class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size):
        """Instantiates a square
        Args:
            size (int): The size of the square
        """
        integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the square
        Returns:
            The area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """Returns the string representation of the square
        Returns:
            The string representation of the square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
