#!/usr/bin/python3
"""
this module use the function add_integer
to add two integers and return the total
"""


def add_integer(a, b=98):
    """this function will add two integers """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a == float("inf") or a == float("-inf"):
        raise OverflowError()
    if b == float("inf") or b == float("-inf"):
        raise OverflowError()
    return int(a + b)
    