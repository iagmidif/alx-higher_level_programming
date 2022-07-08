#!/usr/bin/python3
"""unittest test cases for the module base.py
"""
from models.base import Base
import unittest


class TestIdAssignments(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
