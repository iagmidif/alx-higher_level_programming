#!/usr/bin/python3
""" Module that has a class that inherits from list
"""


class MyList(list):
    """ Class that inherits from list"""

    def __init__(self):
        """ Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """ Prints the sorted list"""
        print(sorted(self))
