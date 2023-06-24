#!/usr/bin/python3
import json
"""Defines a function @load_from_json_file"""


def load_from_json_file(filename):
    """Creates an object from a json file
    Args:
        filename (string): the json file
    Returns:
        The object
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
