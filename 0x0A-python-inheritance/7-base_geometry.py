#!/usr/bin/python3
""" Module that contains the BaseGeometry class
"""


class BaseGeometry:
    """Defines the BaseGeometry class."""

    def __init__(self):
        """Initializes the class."""
        pass

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer"""
        if type(value) is int:
            if value <= 0:
                raise TypeError("{} must be greater than 0".format(name))
        else:
            raise TypeError("{} must be an integer".format(name))
