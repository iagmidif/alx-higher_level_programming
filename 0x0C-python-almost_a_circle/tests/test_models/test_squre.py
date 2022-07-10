"""unittest module for the module square.py
"""
from models.square import Square
from models.base import Base
from unittest import TestCase
from unittest.mock import patch
from io import StringIO


class TestSquareAttributes(TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_ids(self):
        self.assertEqual(Square(1).id, 1)
        self.assertEqual(Square(1, 0, 0, 12).id, 12)
        self.assertEqual(Square(2).id, 2)

    def test_width(self):
        self.assertEqual(Square(10).width, 10)

    def test_height(self):
        self.assertEqual(Square(2).height, 2)

    def test_x(self):
        self.assertEqual(Square(10).x, 0)
        self.assertEqual(Square(10, 5).x, 5)

    def test_y(self):
        self.assertEqual(Square(10).y, 0)
        self.assertEqual(Square(10, 5).y, 0)
        self.assertEqual(Square(10, 5, 6).y, 6)

    def test_width_height_x_y(self):
        self.assertEqual(Square(9, 1, 2).width, 9)
        self.assertEqual(Square(9, 1, 2).height, 9)
        self.assertEqual(Square(9, 1, 2).x, 1)
        self.assertEqual(Square(9, 1, 2).y, 2)

    def test_size_missing(self):
        args = ()
        self.assertRaises(TypeError, Square, *args)

    def test_float_size(self):
        args = (1.5,)
        self.assertRaises(TypeError, Square, *args)

    def test_str_size(self):
        args = ("hello")
        self.assertRaises(TypeError, Square, *args)

    def test_negative_size(self):
        args = (-1, 0, 0)
        self.assertRaises(ValueError, Square, *args)

    def test_zero_size(self):
        args = (0, 0, 0)
        self.assertRaises(ValueError, Square, *args)

    def test_float_x(self):
        args = (1, 1.3)
        self.assertRaises(TypeError, Square, *args)

    def test_str_x(self):
        args = (1, "hello")
        self.assertRaises(TypeError, Square, *args)

    def test_negative_x(self):
        args = (1, -1, 0)
        self.assertRaises(ValueError, Square, *args)

    def test_float_y(self):
        args = (1, 1, 0.8)
        self.assertRaises(TypeError, Square, *args)

    def test_str_y(self):
        args = (1, 1, "hello")
        self.assertRaises(TypeError, Square, *args)

    def test_negative_y(self):
        args = (1, 0, -1)
        self.assertRaises(ValueError, Square, *args)

    def test_area(self):
        self.assertEqual(Square(10).area(), 100)

    def test_display_1x1(self):
        expected = "#\n"
        r1 = Square(1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_display_3x3(self):
        expected = "###\n###\n###\n"
        r1 = Square(3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_print(self):
        expected = "[Square] (1) 1/2 - 3\n"
        r1 = Square(3, 1, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_str(self):
        expected = "[Square] (11) 1/0 - 2"
        r1 = Square(2, 1, 0, 11)
        self.assertEqual(str(r1), expected)

    def test_display_1x1_2_2(self):
        expected = "\n\n  #\n"
        r1 = Square(1, 2, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_display_3x3_3_4(self):
        expected = "\n\n\n\n   ###\n   ###\n   ###\n"
        r1 = Square(3, 3, 4)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), expected)


class TestSquareUpdateArgs(TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
        self.r1 = Square(10, 10, 10, 10)

    def test_update_id_none_args(self):
        self.r1.update(None)
        self.assertEqual(str(self.r1), "[Square] (1) 10/10 - 10")

    def test_update_id_arg(self):
        self.r1.update(89)
        self.assertEqual(str(self.r1), "[Square] (89) 10/10 - 10")

    def test_update_size(self):
        self.r1.update(89, 2)
        self.assertEqual(str(self.r1), "[Square] (89) 10/10 - 2")

    def test_update_three_args(self):
        self.r1.update(89, 2, 4)
        self.assertEqual(str(self.r1), "[Square] (89) 4/10 - 2")

    def test_update_five_args(self):
        self.r1.update(89, 2, 4, 5)
        self.assertEqual(str(self.r1), "[Square] (89) 4/5 - 2")


class TestSquareUpdateKwargs(TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
        self.r1 = Square(10, 10, 10, 10)

    def test_update_id_none_kwargs(self):
        self.r1.update(id=None)
        self.assertEqual(str(self.r1), "[Square] (1) 10/10 - 10")

    def test_update_id_kwargs(self):
        self.r1.update(id=89)
        self.assertEqual(str(self.r1), "[Square] (89) 10/10 - 10")

    def test_update_two_kwargs(self):
        self.r1.update(id=89, size=2)
        self.assertEqual(str(self.r1), "[Square] (89) 10/10 - 2")

    def test_update_three_kwargs(self):
        self.r1.update(id=89, size=2, x=4)
        self.assertEqual(str(self.r1), "[Square] (89) 4/10 - 2")

    def test_update_four_kwargs(self):
        self.r1.update(id=89, size=2, x=4, y=5)
        self.assertEqual(str(self.r1), "[Square] (89) 4/5 - 2")

    def test_update_too_many_kwargs(self):
        self.r1.update(id=89, size=2, x=4, y=5, hello=1, school=5)
        self.assertEqual(str(self.r1), "[Square] (89) 4/5 - 2")
