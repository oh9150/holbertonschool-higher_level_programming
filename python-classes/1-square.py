#!/usr/bin/python3
"""Defines a class Square"""
class Square:
    """Defines a square"""
    def __init__(self, size):
        """Initializes a square with a private attribute size
        Args:
            size(int): the size of the square
        """
        self.__size = size
