#!/usr/bin/python3
"""
This module defines a function that adds two numbers
"""


def add_integer(a, b=98):
    """Function that adds two numbers

    Args:
        a (int or float): first number
        b (int or float, default=98): second number

    Return:
        the addition of a and b, (integer)
    """
    if type(a) in [int, float]:
        try:
            a = int(a)
        except Exception:
            raise TypeError("a must be an integer")
    else:
        raise TypeError("a must be an integer")

    if type(b) in [int, float]:
        try:
            b = int(b)
        except Exception:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("b must be an integer")

    return a + b
