#!/usr/bin/python3
"""Defines a class Square"""
class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes the square
        Args:
            size (int): The size of the square
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

