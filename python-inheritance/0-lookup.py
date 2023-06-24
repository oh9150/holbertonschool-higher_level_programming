#!/usr/bin/python3
"""Defines a function @lookup"""

def lookup(obj):
    """Returns All the attributes and methods in an object
    Args:
        obj (object): the object
    Returns:
        A list containing all the methods and attributes of said object
    """
    return dir(obj)
