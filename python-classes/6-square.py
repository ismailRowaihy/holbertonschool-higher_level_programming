#!/usr/bin/python3
"""
this module is an emptiy class
"""


class Square:
    """a squre class"""
    def __init__(self, size=0, position=(0, 0)):
        """ initilize function"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """a getter function for size"""
        return self.__size

    @property
    def position(self):
        """a getter function for position"""
        return self.__position

    @size.setter
    def size(self, value):
        """a setter function for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """a setter for position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple of 2 " +
                                "positive integers")
        self.__position = value

    def area(self):
        """a function that returns the area of square"""
        return self.__size ** 2

    def my_print(self):
        """a function that prints a # = to size"""
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print("")
        for i in range(self.__size):
            if self.__position[0] > 0:
                print(" " * self.__position[0], end="")
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
