#!/usr/bin/python3
"""this Module is a function
that opens and reads then prints a file"""


def read_file(filename=""):
    """a function that opens and reads then prints a file"""

    with open(filename, mode="r", encoding="UTF-8") as file:
        txt = file.read()
        print(txt)
