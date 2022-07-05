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
