#!/usr/bin/python3
"""This module contains the Rectangle class that inherits for Base
"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle base on the class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor for Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter function for the private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter function for the private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter function for the private attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >=  0")
        self.__x = value

    @property
    def y(self):
        """Getter function for the private attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """Sets the str/print behaviour of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width, self.height)

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle to stdout using `#`"""
        for i in range(self.__height):
            print("#" * self.__width)
