#!/usr/bin/python3
"""
This module contains a function that prints a text with custom indents
"""


def text_indentation(text):
    """ A function that prints a text with 2 new lines after each of
    these characters: `.`, `?`, `:`

    Args:
        text (string): text to be printed
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for c in text:
        if c != " ":
            print(c, end="")
        if c in [".", "?", ":"]:
            print("\n")

