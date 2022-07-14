#!/usr/bin/python3
"""This module contains the base class
"""
import json
import csv
import turtle


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
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
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
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                reader = csv.DictReader(f, fieldnames=fields)
                dcts = [dict([k, int(v)] for k, v in m.items())
                        for m in reader]
                return [cls.create(**dct) for dct in dcts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangels and Squares
        Uses the open library turtle
        For more on how it works please read the README file
        on the root of this projects's directory
        """
        shapes = []
        if list_rectangles is not None and len(list_rectangles) > 0:
            shapes.extend(list_rectangles)
        if list_squares is not None and len(list_squares) > 0:
            shapes.extend(list_squares)
        if len(shapes) > 0:
            t = turtle.Turtle(visible=False)
            screen = turtle.Screen()
            turtle.bgcolor("white")
            t.color("orange")
            t.speed(10)

            t.penup()
            t.goto(10 - screen.window_width() // 2,
                   screen.window_height() // 2 - 10)
            t.pendown()
            highest_height = 0
            total_height = 0
            for i in range(len(shapes)):
                width = shapes[i].width * 2
                height = shapes[i].height * 2
                if highest_height < height:
                    highest_height = height
                t.begin_fill()
                for _ in range(2):
                    t.fd(width)
                    t.rt(90)
                    t.fd(height)
                    t.rt(90)
                t.end_fill()
                t.penup()
                try:
                    if shapes[i + 1].width * 2 <= (
                       screen.window_width() // 2 - t.xcor() - width - 15):
                        t.fd(width + 5)
                    else:
                        total_height += highest_height + 5
                        t.goto(10 - screen.window_width() // 2,
                               screen.window_height() // 2 - 10 - total_height)
                        highest_height = 0
                except IndexError:
                    pass
                t.pendown()
            turtle.done()
