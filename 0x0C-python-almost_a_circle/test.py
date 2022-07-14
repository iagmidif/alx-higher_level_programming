from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

list_rectangels = [Rectangle(10, 10), Rectangle(17, 25), Rectangle(22, 13),
                   Rectangle(18, 6), Rectangle(10, 10), Rectangle(17, 25),
                   Rectangle(22, 13), Rectangle(18, 6)]
list_squares = [Square(10), Square(50), Square(30), Square(45), Square(25),
                Square(10), Square(50), Square(30), Square(45), Square(25)]

Base.draw(list_rectangels, list_squares)
