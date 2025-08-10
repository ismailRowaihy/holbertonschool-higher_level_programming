#!/usr/bin/python3
"""this Module is a function
that creates an Object from a JSON file"""

import json


def load_from_json_file(filename):
    """a function that creates an Object from a JSON file"""

    with open(filename, mode="r", encoding="UTF-8") as file:
        return json.load(file)
