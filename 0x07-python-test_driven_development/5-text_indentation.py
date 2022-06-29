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
    for i in range(len(text)):
        if text[i] == " " and \
                (i == len(text) - 1 or i == 1 or text[i-1] in [".", "?", ":"]):
            continue
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n")
