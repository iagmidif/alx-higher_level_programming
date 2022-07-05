#!/usr/bin/python3
"""Module that contain a function that uses the json module
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (str)"""
    return json.dumps(my_obj)
