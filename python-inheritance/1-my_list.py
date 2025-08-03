#!/usr/bin/python3
"""this Module is a class that inherits from list """


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
