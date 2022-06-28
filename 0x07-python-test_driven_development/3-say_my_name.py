#!/usr/bin/python3
"""
A module that contains a function that prints information to the screen
"""


def say_my_name(first_name, last_name=""):
    """ Function that prints:
    `Write a function that prints My name is <first name> <last name>`

    Args:
        first_name (string): first name to be printed
        last_name (string, default=""): last name to be used
    """
    if type(first_name) is str:
        if type(last_name) is  str:
            print("My name is {} {}".format(first_name, last_name))
        else:
            raise TypeError("last_name must be a string")
    else:
        raise TypeError("first_name must be a string")
