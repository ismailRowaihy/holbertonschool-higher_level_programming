#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            data = list(csv.DictReader(file))
        with open("data.json", mode="w", encoding="utf-8") as jfile:
            json.dump(data, jfile)
        return True
    except Exception:
        return False
