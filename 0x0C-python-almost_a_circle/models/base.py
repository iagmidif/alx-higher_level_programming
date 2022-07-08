#!/usr/bin/python3
"""This module contains the base class
"""


class Base:
    """This class is the base of all other classes in this project.
    The goal of it is to manage `id` attribute in all the classes in this
    project and to avoid duplicating the same code (by extension, same bugs)"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor function"""

        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
