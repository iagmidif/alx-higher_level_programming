#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
print(my_square.__doc__)
print(__import__('0-square').__doc__)
print(Square.__init__.__doc__)
