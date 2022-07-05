#!/usr/bin/python3
"""Module containing a function that writes into a file
"""


def write_file(filename="", text=""):
    """Function that writes into a function
    Args:
        filename (str): name of the file to write to
        text (str): the text to be written

    Returns:
        Number of characters written
    """
    if filename:
        with open(filename, 'w', encoding="utf-8") as f:
            if text:
                return f.write(text)
