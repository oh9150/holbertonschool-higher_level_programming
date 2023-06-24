#!/usr/bin/python3
import json
"""Defines a function from_json_string"""


def from_json_string(my_str):
    """Returns an object from a json string
    Args:
        my_str (string): The json string
    Returns:
        The object made from @my_str
    """
    return json.loads(my_str)
