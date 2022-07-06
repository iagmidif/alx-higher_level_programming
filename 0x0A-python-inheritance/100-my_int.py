#!/usr/bin/python3
"""Module that contains a class that inherits from int
"""


class MyInt(int):
    """A class that inherits form int"""

    def __eq__(self, other):
        """Defines the == behaviour"""
        return int(self) != other

    def __ne__(self, other):
        """Defines the != behaviour"""
        return int(self) == other
