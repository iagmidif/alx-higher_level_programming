#!/usr/bin/python3
"""Module that contain a function that append to a file
"""


def append_write(filename="", text=""):
    """Function that append a text to a file"""
    if filename:
        with open(filename, 'a', encoding="utf-8") as f:
            if text:
                return f.write(text)
