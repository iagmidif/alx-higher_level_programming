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

    @property
    def position(slef):
        """
        Getter function for the private attribute position

        Args:

        Returns:
            the value of the priate attribute position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter function for the private attribute position

        Args:
            value (tuple): value to be set for position

        Returns:
        """
        if type(value) is tuple and len(value) is 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        A function that prints the square in stdout with the character #

        Args:

        Returns:
        """
        if self.__size == 0:
            print()
        for y in range(self.__position[1]):
            print()
        for row in range(self.__size):
            for x in range(self.__position[0]):
                print(' ', end='')
            for i in range(self.__size):
                print("#", end='')
            print()
