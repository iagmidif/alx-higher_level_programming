#!/usr/bin/python3
"""This module contains the base class
"""
import json
import csv


class Base:
    """This class is the base of all other classes in this project.
    The goal of it is to manage `id` attribute in all the classes in this
    project and to avoid duplicating the same code (by extension, same bugs)"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor function"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Retursn the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of a `list_objs` to a file"""
        lst = []
        if list_objs is not None or len(list_objs) > 0:
            for obj in list_objs:
                lst.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation `json_string´"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all the attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 2)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                json_file = Base.from_json_string(f.read())
                return [cls.create(**dct) for dct in json_file]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""
        fields = []
        with open(cls.__name__ + ".csv", "w") as f:
            if list_objs is None or len(list_objs) <= 0:
                f.write("[]")
            else:
                if cls.__name__ is "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ is "Square":
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV"""
        fields = []
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                if cls.__name__ is "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ is "Square":
                    fields = ["id", "size", "x", "y"]
                reader = csv.DictReader(f, fieldnames=fields)
                dcts = [dict([k, int(v)] for k, v in m.items())
                        for m in reader]
                return [cls.create(**dct) for dct in dcts]
        except IOError:
            return []
