#!/usr/bin/python3
"""
Module that defines the class Rectangle
"""


class Rectangle:
    """A class that defines a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Instantiation method

        Args:
            width (int, default=0): represents the width of the rectangle
            height (int, default=0): represents the height of the rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter method for the private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Getter method for the private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method that calculates the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ Method that calculates the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((2 * self.__height) + (2 * self.__width))

    def __str__(self):
        """ Defines the behavior of str and print"""
        if self.__height == 0 or self.__width == 0:
            return ""
        data_str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                data_str += '#'
            if row < self.__height - 1:
                data_str += '\n'
        return data_str

    def __repr__(self):
        """ Defines the behavior of repr for the Reactangle object"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ Prints a message when the Rectangke object is deleted using del"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
