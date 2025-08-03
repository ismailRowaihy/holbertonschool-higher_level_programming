#!/usr/bin/python3
"""this Module is a function that
return is an object is an instance of a class """


def inherits_from(obj, a_class):
    """this Module is a function that
    return is an object is an instance of a class"""
    return type(obj) is not a_class and isinstance(obj,a_class)


a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))