#!/usr/bin/python3
"""
this module use the function matrix_divided
to divide a matrix  and return the new matrix
"""


def matrix_divided(matrix, div):
    """divide a matrix  and return the new matrix """
    new_matrix = []
    size_of_list = 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for i in range(len(matrix)):
        new_matrix.append(list())
        if i == 0:
            size_of_list = len(matrix[i])
        if size_of_list != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        for j in matrix[i]:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            if div == float("inf"):
                new_matrix[i].append(0.0)
            else:
                new_matrix[i].append(round(j / div, 2))
    return new_matrix
