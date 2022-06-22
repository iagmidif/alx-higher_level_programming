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
        self.__size = size

    def area(self):
        """
        A public instance method

        Args:

        Returns:
            the area of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        Getter function for the private attribute size

        Args:

        Returns:
            the value of the private attribute size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter function for the private attribute size

        Args:
            value (int): value to be set for size

        Returns:
        """
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """
        A function that prints the square in stdout with the character #

        Args:

        Returns:
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
