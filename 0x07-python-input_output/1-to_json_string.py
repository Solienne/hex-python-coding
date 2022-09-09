#!/usr/bin/python3
"""Defines function to_json_string"""

import json


def to_json_string(my_obj):
    """
    Returns JSON representation of object (string).
    Args:
        my_obj (string): string that will be converted to JSON
    Return:
        JSON representation of string
    """
    return json.dumps(my_obj)
