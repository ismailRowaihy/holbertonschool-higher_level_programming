#!/usr/bin/python3
"""this Module is a function
that converts json text to dict"""

import json


def from_json_string(my_str):
    """a functionthat converts json text to dict"""
    return json.loads(my_str)
