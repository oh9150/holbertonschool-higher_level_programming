#!/usr/bin/python3
"""Defines a function @is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Returns True if @obj is an instance of @a_class, or if @obj is an
    instance of a class that inherited from a_class, else, False.
    Args:
        obj: The object to compare
        a_class (class): The class to compare
    Returns:
        See above...
    """
    return isinstance(obj, a_class)
