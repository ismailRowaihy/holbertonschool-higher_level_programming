#!/usr/bin/python3
"""this Module is a function
that opens and appends to a file"""


def append_write(filename="", text=""):
    """a function that opens and appends to a file"""

    with open(filename, mode="a", encoding="UTF-8") as file:
        return file.write(text)
