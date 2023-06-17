#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Defines a rectangle
    Attributes:
        number_of_instances (int): the ammount of current rectangle instances
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantaties a rectangle with the given parameters, and adds 1 to
        number_of_instances
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Prints "Bye rectangle..." when an instance of this class, and
        subtracts 1 from number_of_instances when an instance of this class
        is being deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area, if either of them
        isn't an instance of Rectangle, raises a TypeError, if the area of
        rect_1 == rect_2, returns rect_1
        Returns:
            The bigger rectangle, if the area of rect_1 == rect_2, returns
            rect_1
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    def __str__(self):
        """Returns the string to print using print() or str()
        Returns:
            The string to print
        """
        retstr = ""
        if self.height <= 0 or self.width <= 0:
            return retstr
        for height in range(self.height):
            for width in range(self.width):
                retstr += str(self.print_symbol)
            retstr += "\n"
        return retstr[:-1]

    def __repr__(self):
        """Returns the repr() representation of the object
        Returns:
            The repr() representation of the object
        """
        return "Rectangle({}, {})".format(self.width, self.height)
