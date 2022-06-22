#!/usr/bin/python3
"""
Module that defines a Square class
"""


class Square:
    """
    A class that defines a Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation function"""
        self.__size = size
        self.__position = position

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
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(slef):
        """
        Getter function for the private attribute position
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) is 2 \
                and type(value[0]) is int and type(value[1]) \
                and value[0] >= 0 and value[0] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        A function that prints the square in stdout with the character #
        """
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print("#" * self.__size)
        else:
            print()
