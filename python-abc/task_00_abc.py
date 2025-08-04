#!/usr/bin/env python3
"""this Module is about learning abc class """


from abc import ABC, abstractmethod


class animal(ABC):
    """an abstract class"""

    @abstractmethod
    def sound(self):
        pass


class Dog(animal):
    """a class inherits from an abstract class"""

    def sound(self):
        return "BARK"


class Cat(animal):
    """a class inherits from an abstract class"""

    def sound(self):
        return "Meow"
