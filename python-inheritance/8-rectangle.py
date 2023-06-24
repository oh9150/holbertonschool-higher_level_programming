#!/usr/bin/python3
"""Defines a class Rectangle"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry
class Rectangle(BaseGeometry):
    """Defines a Rectangle"""

    def __init__(self, width, height):
        """Initializes a Rectangle
        Args:
            width (int): The width
            height (int): The height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
