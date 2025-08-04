#!/usr/bin/env python3
"""this Module is about learning abc class """


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """an abstract class"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """a circle class that inherits from shape"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """a Rectangle class that inherits from shape"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if (self.width * self.width) == 0:
            return 0
        return 2 * (self.width + self.height)


def shape_info(obj):
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
