#!/usr/bin/python3
"""Module that contains a function that uses the json module
"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj: object to be serialize
        filename: the name of the file to be used
    """
    if filename:
        with open(filename, 'w') as f:
            json.dump(my_obj, f)
