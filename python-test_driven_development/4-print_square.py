#!/usr/bin/python3
"""
this module use the function matrix_divided
to divide a matrix  and return the new matrix
"""


def print_square(size):
    """divide a matrix  and return the new matrix """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
