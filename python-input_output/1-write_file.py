#!/usr/bin/python3
"""Defines a function write_file"""


def write_file(filename="", text=""):
    """Writes @text into the file @filename
    Args:
        filename (string): The filename
        text (string): The text to write
    Returns:
        The ammount of characters written
    """
    with open(filename, mode="w", enconding="utf-8") as f:
        return f.write(text)
