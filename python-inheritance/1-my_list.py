#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """Adds a print_sorted method that prints the sorted list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending)"""
        print(sorted(self))
