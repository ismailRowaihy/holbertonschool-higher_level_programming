#!/usr/bin/python3
"""this Module is a function that
return is an object is an instance of a class """


def inherits_from(obj, a_class):
    """this Module is a function that
    return is an object is an instance of a class"""
    return type(obj) is not a_class and isinstance(obj, a_class)
