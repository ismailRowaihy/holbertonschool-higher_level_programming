#!/usr/bin/python3
"""this Module is a class
student that has a func to json"""


class Student:
    """a class student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
