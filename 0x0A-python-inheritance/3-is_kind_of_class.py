#!/usr/bin/python3
""" Module that have a finction that uses isinstance
"""


def is_kind_of_class(obj, a_class):
    """ Uses isinstance

    Returns: True if the object is an instance of, or if the object is an
             instance of a class that inherited from the specified class
    """
    return isinstance(obj, a_class)
