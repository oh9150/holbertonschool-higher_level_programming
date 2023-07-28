#!/usr/bin/python3
"""Defines a function add_integer"""

def add_integer(a, b=89):
    """Adds two integers, if either of them is not an int or float,
    raises a TypeError
    Args:
        a (int, float): num #1
        b (int, float): num #2
    Returns:
        The sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
