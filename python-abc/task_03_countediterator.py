#!/usr/bin/python3
"""this Module is about learning abc class """


class CountedIterator:
    def __init__(self, iterator, count=0):
        self.iterator = iter(iterator)
        self.count = count

    def __next__(self):
        self.count += 1
        return next(self.iterator)

    def get_count(self):
        return self.count
