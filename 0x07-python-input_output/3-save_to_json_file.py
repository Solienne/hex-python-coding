#!/usr/bin/python3
"""Defines function save_to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes Object to a text file, using JSON representation.
    Args:
        my_obj: string  that will be converted to JSON
        filename: name of the file where object will be saved
    Return:
        JSON representation of string
    """
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
