#!/usr/bin/python3
"""
This module contains a function that prints a square
"""


def print_square(size):
    """ A functions that prints a square with the character #

    Args:
        size (int): length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#" * size)
