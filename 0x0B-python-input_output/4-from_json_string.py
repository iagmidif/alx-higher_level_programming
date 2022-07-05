#!/usr/bin/python3
"""Module that contain a function that uses the json module
"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string"""
    return json.loads(my_str)
