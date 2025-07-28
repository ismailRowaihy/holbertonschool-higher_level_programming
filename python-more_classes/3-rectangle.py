#!/usr/bin/python3
"""
this module is an emptiy class
"""


class Rectangle:
    """a Rectangle  class"""
    def __init__(self, width=0, height=0):
        """ initilize function"""
        self.width = width
        self.height = height

    def __str__(self):
        if (self.__height * self.__width) == 0:
            return ""
        else:
            for i in range(self.__height):
                if i == self.__height - 1:
                    print("#" * self.__width, end="")
                else:
                    print("#" * self.__width)
        return ""

    @property
    def width(self):
        """a getter for width"""
        return self.__width

    @property
    def height(self):
        """a getter for height"""
        return self.__height

    @width.setter
    def width(self, value):
        """a setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """a setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if (self.__height * self.__width) == 0:
            return 0
        return 2 * (self.__height + self.__width)
