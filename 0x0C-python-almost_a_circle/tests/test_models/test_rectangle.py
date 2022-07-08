#!/usr/bin/python3
"""unittest test cases for the module rectangle.py
"""
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestRectangleAttributes(unittest.TestCase):

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
