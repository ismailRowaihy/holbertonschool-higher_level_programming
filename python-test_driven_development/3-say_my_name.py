#!/usr/bin/python3
"""
this module use the function ay_my_name
to return the complete name
"""


def say_my_name(first_name, last_name=""):
    """ return the complete name """
    if not isinstance(first_name, str) and not isinstance(last_name, str):
        raise TypeError
    elif not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
