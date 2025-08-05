#!/usr/bin/python3
"""this Module is about learning abc class """


class VerboseList(list):
    """an VerboseList class"""

    def __init__(self, aList):
        super().__init__(aList)

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        super().extend(x)
        print(f"Extended the list with [{len(x)}] items.")

    def remove(self, item):
        if item not in self:
            return None
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, item=None):
        if item is not None:
            print(f"Popped [{super().pop(item)}] from the list.")
        else:
            print(f"Popped [{super().pop()}] from the list.")
