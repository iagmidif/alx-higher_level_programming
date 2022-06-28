#!/usr/bin/python3
""" A module that contains a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """ A function that validates 2 matrices
    and returns m_a * m_b form the function `multiply_matrices`
    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix

    Returns:
        the multiplication of the two matrices m_a and m_b
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for item in m_a:
        if type(item) is not list:
            raise TypeError("m_a must be a list of lists")
    for item in m_b:
        if type(item) is not list:
            raise TypeError("m_b  must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    row_len = len(m_a[0])
    for row in m_a:
        if len(row) != row_len:
            raise TypeError("each row of m_a must be of the same size")
    row_len = len(m_b[0])
    for row in m_b:
        if len(row) != row_len:
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return multiply_matrices(m_a, m_b)


def multiply_matrices(m_a, m_b):
    """ A function that multiplies 2 matrices

    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix

    Returns:
        the multiplication of the two matrices m_a and m_b
    """
    result = [ [] for _ in range(len(m_a)) ]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            n = 0
            for k in range(len(m_b)):
                n += (m_a[i][k] * m_b[k][j])
            result[i].append(n)
    return result
