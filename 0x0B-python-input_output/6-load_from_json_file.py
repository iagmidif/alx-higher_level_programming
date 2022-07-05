#!/usr/bin/python3
"""Module that contains a function that uses the json module
"""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a JSON file"""
    if filename:
        with open(filename) as f:
            return json.load(f)
