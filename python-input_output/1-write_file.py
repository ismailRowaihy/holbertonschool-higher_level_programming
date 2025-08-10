#!/usr/bin/python3
"""this Module is a function
that opens and writes to a file"""


def write_file(filename="", text=""):
    """a function that opens and rwrites to a file"""

    with open(filename, mode="w", encoding="UTF-8") as file:
        return file.write(text)
