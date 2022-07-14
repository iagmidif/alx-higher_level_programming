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
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        """Getter function for the attribute size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This method is used to update the Square attributes"""
        attributes = {}
        if args is not None and len(args) > 0:
            keys = ["id", "size", "x", "y"]
            for i in range(len(args) if len(args) < 5 else 5):
                attributes[keys[i]] = args[i]
        else:
            attributes = kwargs

        if len(attributes) > 0:
            for key, value in attributes.items():
                if key == "id" and value is None:
                    self.__init__(self.size,  self.x, self.y)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        return {
            "id": self.id, "size": self.size, "x": self.x,
            "y": self.y
        }
