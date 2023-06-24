#!/usr/bin/python3
"""Defines a function @is_same_class"""


def is_same_class(obj, a_class):
    """Returns True of @obj is the same type as @a_class, False otherwise
    Args:
        obj: The object to compare
        a_class (class): A class to compare
    Returns:
        True if @obj is the same type as @a_class, False otherwise
    """
    return(type(obj) == a_class)
