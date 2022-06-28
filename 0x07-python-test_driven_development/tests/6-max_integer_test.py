#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ The testcase used for unittesting max_integer([..])
    """

    def test_max(self):
        """ Tests for the correct output given a valid list
        """
        self.assertEqual(10, max_integer([2, 5, 1, 10]))
        self.assertEqual(10, max_integer([10, 2, 5, 1]))
        self.assertEqual(5, max_integer([2, 5, 1, -10]))
        self.assertEqual(None, max_integer([]))
        self.assertEqual(None, max_integer([None]))
        self.assertEqual(7, max_integer([7]))
        self.assertEqual(float("inf"), max_integer([5, 1, float("inf"), 7]))
        self.assertEqual(7, max_integer([5, 1, -float("inf"), 7]))

    def test_types(self):
        """ Tests for wrong data types
        """
        self.assertRaises(TypeError, max_integer, [2, 5, 1, "hello"])
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
