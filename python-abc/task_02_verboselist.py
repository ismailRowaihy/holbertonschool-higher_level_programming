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
        print(f"Extended the list with [{x}] items.")

    def remove(self, item):
        if item not in self:
            return None
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, item=None):
        if item is not None:
            item = super().pop(item)
            print(f"Popped [{item}] from the list.")
        else:
            item = super().pop()
            print(f"Popped [{item}] from the list.")
