#!/usr/bin/python3
"""Rectangles Module, based on 7-base_geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangles class"""

    def __init__(self, width, height):
        """Instantiation of the Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Defines the str behavior"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """Computes the area of a rectangle"""
        return self.__width * self.__height
