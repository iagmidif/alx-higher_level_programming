#!/usr/bin/python3
"""unittest test cases for the module rectangle.py
"""
from models.base import Base
from models.rectangle import Rectangle
from unittest import TestCase
from unittest.mock import patch
from io import StringIO


class TestRectangleAttributes(TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_ids(self):
        self.assertEqual(Rectangle(1, 2).id, 1)
        self.assertEqual(Rectangle(1, 2, 0, 0, 12).id, 12)
        self.assertEqual(Rectangle(2, 1).id, 2)

    def test_width(self):
        self.assertEqual(Rectangle(10, 2).width, 10)

    def test_height(self):
        self.assertEqual(Rectangle(2, 10).height, 10)

    def test_x(self):
        self.assertEqual(Rectangle(10, 2).x, 0)
        self.assertEqual(Rectangle(10, 2, 5).x, 5)

    def test_y(self):
        self.assertEqual(Rectangle(10, 2).y, 0)
        self.assertEqual(Rectangle(10, 2, 5).y, 0)
        self.assertEqual(Rectangle(10, 2, 5, 6).y, 6)

    def test_width_height_x_y(self):
        self.assertEqual(Rectangle(9, 4, 1, 2).width, 9)
        self.assertEqual(Rectangle(9, 4, 1, 2).height, 4)
        self.assertEqual(Rectangle(9, 4, 1, 2).x, 1)
        self.assertEqual(Rectangle(9, 4, 1, 2).y, 2)

    def test_two_args_missing(self):
        args = ()
        self.assertRaises(TypeError, Rectangle, *args)

    def test_one_arg_missing(self):
        args = (2,)
        self.assertRaises(TypeError, Rectangle, *args)

    def test_float_width(self):
        args = (1.5, 3)
        self.assertRaises(TypeError, Rectangle, *args)

    def test_str_width(self):
        args = ("hello", 3)
        self.assertRaises(TypeError, Rectangle, *args)

    def test_negative_width(self):
        args = (-1, 1, 0, 0)
        self.assertRaises(ValueError, Rectangle, *args)

    def test_zero_width(self):
        args = (0, 1, 0, 0)
        self.assertRaises(ValueError, Rectangle, *args)

    def test_float_height(self):
        args = (1, 0.5)
        self.assertRaises(TypeError, Rectangle, *args)

    def test_str_height(self):
        args = (1, "hello")
        self.assertRaises(TypeError, Rectangle, *args)

    def test_negative_height(self):
        args = (1, -1, 0, 0)
        self.assertRaises(ValueError, Rectangle, *args)

    def test_zero_height(self):
        args = (1, 0, 0, 0)
        self.assertRaises(ValueError, Rectangle, *args)

    def test_float_x(self):
        args = (1, 3, 1.3)
        self.assertRaises(TypeError, Rectangle, *args)

    def test_str_x(self):
        args = (1, 3, "hello")
        self.assertRaises(TypeError, Rectangle, *args)

    def test_negative_x(self):
        args = (1, 1, -1, 0)
        self.assertRaises(ValueError, Rectangle, *args)

    def test_float_y(self):
        args = (1, 3, 1, 0.8)
        self.assertRaises(TypeError, Rectangle, *args)

    def test_str_y(self):
        args = (1, 3, 1, "hello")
        self.assertRaises(TypeError, Rectangle, *args)

    def test_negative_y(self):
        args = (1, 1, 0, -1)
        self.assertRaises(ValueError, Rectangle, *args)

    def test_area(self):
        self.assertEqual(Rectangle(10, 2).area(), 20)

    def test_display_1x1(self):
        expected = "#\n"
        r1 = Rectangle(1, 1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_display_2x3(self):
        expected = "##\n##\n##\n"
        r1 = Rectangle(2, 3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_print(self):
        expected = "[Rectangle] (1) 1/2 - 3/6\n"
        r1 = Rectangle(3, 6, 1, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_str(self):
        expected = "[Rectangle] (11) 1/0 - 2/4"
        r1 = Rectangle(2, 4, 1, 0, 11)
        self.assertEqual(str(r1), expected)

    def test_display_1x1_2_2(self):
        expected = "\n\n  #\n"
        r1 = Rectangle(1, 1, 2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_display_2x3_3_4(self):
        expected = "\n\n\n\n   ##\n   ##\n   ##\n"
        r1 = Rectangle(2, 3, 3, 4)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected)


class TestRectangleUpdateArgs(TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(10, 10, 10, 10, 10)

    def test_update_id_none_args(self):
        self.r1.update(None)
        self.assertEqual(str(self.r1), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_id_arg(self):
        self.r1.update(89)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_two_args(self):
        self.r1.update(89, 2)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_three_args(self):
        self.r1.update(89, 2, 3)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_four_args(self):
        self.r1.update(89, 2, 3, 4)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_five_args(self):
        self.r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 4/5 - 2/3")


class TestRectangleUpdateKwargs(TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(10, 10, 10, 10, 10)

    def test_update_id_none_kwargs(self):
        self.r1.update(id=None)
        self.assertEqual(str(self.r1), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_id_kwargs(self):
        self.r1.update(id=89)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_two_kwargs(self):
        self.r1.update(id=89, width=2)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_three_kwargs(self):
        self.r1.update(id=89, width=2, height=3)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_four_kwargs(self):
        self.r1.update(id=89, width=2, height=3, x=4)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_five_kwargs(self):
        self.r1.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_too_many_kwargs(self):
        self.r1.update(id=89, width=2, height=3, x=4, y=5, hello=1, school=5)
        self.assertEqual(str(self.r1), "[Rectangle] (89) 4/5 - 2/3")


class Test_Rectangle_to_dict(TestCase):

    def test_to_dictionary(self):
        r1 = Rectangle(2, 3, 4, 5, 89)
        expected = {'width': 2, 'height': 3, 'x': 4, 'y': 5, 'id': 89}
        self.assertDictEqual(r1.to_dictionary(), expected)

    def test_to_dictionary_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 1, 2, 42).to_dictionary(42)
