#!/usr/bin/python3
"""this Module is a class
student that has a func to json"""


class Student:
    """a class student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        for key, value in json.items():
            setatter(self, key, value)
