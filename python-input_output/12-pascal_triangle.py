#!/usr/bin/python3
"""this Module is a function
that returns pascal triangle"""


def pascal_triangle(n):
    """pascal triangle function"""

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):

        oldRow = triangle[-1]
        newRow = [1]

        for j in range(1, i):
            newRow.append(oldRow[j - 1] + oldRow[j])
        newRow.append(1)
        triangle.append(newRow)

    return triangle
