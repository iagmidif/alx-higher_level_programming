#!/usr/bin/python3
"""This module conatins the Square class that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square base on the class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor for the Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Sets the str/print beahviour of the Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width)
