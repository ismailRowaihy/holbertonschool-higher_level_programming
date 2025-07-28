#!/usr/bin/python3
"""
this module is an emptiy class
"""


class Square:
    """a squre class"""
    def __init__(self, size=0):
        """ initilize function"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """a function that returns the area of square"""
        return self.__size ** 2
