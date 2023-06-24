#!/usr/bin/python3
"""Defines a function append_write"""


def append_write(filename="", text=""):
    """Appends @text to the file @filename
    Args:
        filename (string): The filename
        text (string): The text to append to the file
    Returns:
        The number of characters written
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.append(text)
