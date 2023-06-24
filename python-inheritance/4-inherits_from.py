#!/usr/bin/python3
"""Defines a function @inherits_from"""


def inherits_from(obj, a_class):
    """Returns True if @obj is an instance of a class that inherited from
    @a_class, else False
    Args:
        obj: The object to compare
        a_class (class): See above
    Returns:
        See above...
    """
    return issubclass(type(obj), a_class) and not type(obj) == a_class
