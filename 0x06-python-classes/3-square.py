#!/usr/bin/python3
"""
Module that defines a Square class
"""


class Square:
    """
    A class that defines a Square
    """

    def __init__(self, size=0):
        """Instantiation function"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        A public instance method

        Args:

        Returns:
            the area of the square
        """
        return (self.__size ** 2)
