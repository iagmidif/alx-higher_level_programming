#!/usr/bin/python3
"""unittest test cases for the module base.py
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest import TestCase


class TestIdAssignments(TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_unprovided(self):
        self.assertEqual(Base().id, 1)

    def test_id_None(self):
        self.assertEqual(Base(None).id, 1)

    def test_ints(self):
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base(-12).id, -12)

    def test_all_together(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base(-12).id, -12)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(98).id, 98)


class TestToJSONString(TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_json_return_type(self):
        r1 = Rectangle(10, 10)
        s1 = Square(1)
        self.assertIs(str, type(Base.to_json_string([r1.to_dictionary()])))
        self.assertIs(str, type(Base.to_json_string([s1.to_dictionary()])))

    def test_rectangle_to_json(self):
        r1 = Rectangle(10, 7, 2, 8)
        self.assertEqual(len(Base.to_json_string([r1.to_dictionary()])), 53)

    def test_square_to_json(self):
        s1 = Square(2, 3, 4, 5)
        self.assertEqual(len(Base.to_json_string([s1.to_dictionary()])), 38)

    def test_to_json_string_multi_dicts(self):
        r1 = Rectangle(10, 7, 2, 8)
        s1 = Square(2, 3, 4, 5)
        dicts = [r1.to_dictionary(), s1.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(dicts)), 91)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_ro_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_ro_json_string_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string("hello", [1, 2])


class TestSaveToFile(TestCase):

    def tearDown(self):
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass

    def test_save_to_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 53)

    def test_save_to_file_square(self):
        s1 = Square(2, 3, 4, 5)
        Square.save_to_file([s1])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 38)

    def test_save_to_file_multi_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(5, 2, 9, 11)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 106)

    def test_save_to_file_square(self):
        s1 = Square(2, 3, 4, 5)
        s2 = Square(9, 8, 7, 6)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 76)

    def test_save_to_file_overwrite(self):
        r1 = Rectangle(10, 7, 2, 8)
        Square.save_to_file([r1])
        r2 = Rectangle(1, 7, 2, 8)
        Square.save_to_file([r2])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 52)

    def test_save_to_file_empty_lst(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file("hello", [1, 2])


if __name__ == '__main__':
    unittest.main()
