#!/usr/bin/python3
"""this Module is a function
that converts an obj to json text file"""

import json


def save_to_json_file(my_obj, filename):
    """a function that converts an obj to json text file"""

    with open(filename, mode="w", encoding="UTF-8") as file:
        json.dump(my_obj, file)
