#!/usr/bin/python3
""" Module that contains a function that looks up an object
"""


def lookup(obj):
    """ Function that looks up the available
    attributes and methods of an object

    Args:
        obj: object to look up

    Return: a list of available attributes and methods of an object
    """
    return dir(obj)
