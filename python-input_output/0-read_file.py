#!/usr/bin/python3
"""Defines a function read_file"""


def read_file(filename=""):
    """Prints the entire content of the file @filename and prints it to stdout
    Args:
        filename (string): The filename
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
