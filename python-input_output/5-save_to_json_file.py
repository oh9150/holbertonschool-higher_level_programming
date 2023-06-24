#!/usr/bin/python3
import json
"""Defines a function @save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """Converts @my_obj to a json string, then saves it into @filename
    Args:
        my_obj: The object to convert to json
        filename (string): The filename
    """
    with open(filename, mode="w") as f:
        f.dump(my_obj, f)
