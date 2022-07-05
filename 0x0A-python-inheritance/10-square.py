#!/usr/bin/python3
"""Square module base on 9-Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class base on Rectangle"""

    def __init__(self, size):
        """Inistantiation funciton for the class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
