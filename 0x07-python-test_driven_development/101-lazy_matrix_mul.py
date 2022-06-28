#!/usr/bin/python3
""" This module contains a function that mulstiplies
two matrices usign numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ A function that uses numpy to multiply
    two matrices
    """
    return np.dot(m_a, m_b)
