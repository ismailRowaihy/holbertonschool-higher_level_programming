#!/usr/bin/python3
"""this Module is a empty class """


class BaseGeometry:
    """empty class for now"""

    def __init__(self):
        self

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        self.name = name
        if type(value) is not int:
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
