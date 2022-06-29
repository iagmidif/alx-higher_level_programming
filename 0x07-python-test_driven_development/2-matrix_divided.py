#!/usr/bin/python3
"""
This odule contains a fucntion that divides all
elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Function that devides all elements of a matrix

    Args:
        matrix (list of lists): matrix to be used
        div (integer or float): the number that will be used to divide

    Returns:
        a new matrix
    """
    matrix_typeE = "matrix must be a matrix (list of lists) of integers/floats"
    row_len_e = "Each row of the matrix must have the same size"
    div_type_e = "div must be a number"
    div_zero_e = "division by zero"

    if type(matrix) is not list:
        raise TypeError(matrix_typeE)

    row_len = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(matrix_typeE)
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(matrix_typeE)
        if len(row) != row_len and row_len != 0:
            raise TypeError(row_len_e)
        row_len = len(row)

    if type(div) not in [int, float]:
        raise TypeError(div_type_e)
    if div == 0:
        raise ZeroDivisionError(div_zero_e)

    return [[round(i / div, 2) for i in row] for row in matrix]
