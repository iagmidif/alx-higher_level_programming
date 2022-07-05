#!/usr/bin/python3
"""Module that contain a function that reads a file
"""


def read_file(filename=""):
    """Function that reads a file and prints our to stdout"""
    if filename:
        with open(filename, 'r', encoding="utf-8") as f:
            print(f.read(), end="")
