#!/usr/bin/python3
"""this Module is a Rectangle class """


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


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height


print(issubclass(Rectangle, BaseGeometry))