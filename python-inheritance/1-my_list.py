#!/usr/bin/python3
"""this Module is a class that inherits class list """


class MyList(list):
    """a class that ingerits class list"""
    def print_sorted(self):
        print(sorted(self))
