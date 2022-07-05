#!/usr/bin/python3
""" Module that have a function that uses type() 
"""


def is_same_class(obj, a_class):
    """ Uses type()

    Args:
        obj: the object to be checked
        a_class: the class to be used

    Return: True if the object is exactly an instance of the class
            False otherwise
    """
    return type(obj) is a_class
