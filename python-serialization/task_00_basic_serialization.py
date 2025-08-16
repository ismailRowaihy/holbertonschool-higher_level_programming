#!/usr/bin/python3

import json


def serialize_and_save_to_file(data, filename):
    """serialize python dict and save to file"""

    with open(filename, mode="w", encoding="UTF-8") as file:
        return json.dump(data, file)


def load_and_deserialize(filename):
    """deserialize json file into python dict"""

    with open(filename, mode="r", encoding="UTF-8") as file:
        return json.load(file)
