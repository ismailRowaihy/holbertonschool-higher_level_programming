#!/usr/bin/python3
"""this Module is a function
that creates an Object from a JSON file"""

import json
import sys


load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


try:
    old_file = load_from_json_file("add_item.json")
except:
    old_file = []

alist = old_file + [args for args in sys.argv[1:]]
save_to_json_file(alist,"add_item.json")

