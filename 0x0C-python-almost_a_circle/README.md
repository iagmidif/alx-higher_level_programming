## 0x0C-python-almost_a_circle

This project span around reviewing concepts we have already learn like:
- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file

And also we needed to look onto new concepts to complete this project like:
- `args` and `kwargs`
- Serialization/Deserializaition
- JSON


So, the whole project, in short, was about creating a **base class** which is in the file [base.py](https://github.com/iagmidif/alx-higher_level_programming/blob/main/0x0C-python-almost_a_circle/models/base.py), that defines methods and attributes like *object id*, *json serialization*, *json deserialization*, *saving and loading from regular and csv file*, and [draw](https://github.com/iagmidif/alx-higher_level_programming/tree/main/0x0C-python-almost_a_circle#the-draw-method) *(which is detailed below*.


And then creating a **rectangle class** which is in the file [rectangle.py](https://github.com/iagmidif/alx-higher_level_programming/blob/main/0x0C-python-almost_a_circle/models/rectangle.py), that inherits from [Base](https://github.com/iagmidif/alx-higher_level_programming/blob/main/0x0C-python-almost_a_circle/models/base.py) and also defines more methods and attributes like the rectangle's *height*, *width*, *x position*, *y position*, *updating a rectangle*, *serializing*, *and display*.


Finally, the **square class** which is in the file [square.py](https://github.com/iagmidif/alx-higher_level_programming/blob/main/0x0C-python-almost_a_circle/models/square), which inherits from [Rectangle](https://github.com/iagmidif/alx-higher_level_programming/blob/main/0x0C-python-almost_a_circle/models/rectangle.py), and modifies some methods and attributes to fit the *square*.


### The *draw()* method

This static method accepts two arguments `*list_rectangles*` and `*list_square*` which as their names suggest, they are list of *Rectangle* and list of *Square* objects respectively.


```def draw(list_rectangles, list_squares):```


Then ` draw() ` will draw the objects (i.e. Rectangles and Squares, if any) using the [Python Turtle module](https://docs.python.org/2/library/turtle.html) to open a new window and draw the shapes.

The shapes will be drawn horizontally as long as the window's width allows it and then the drawing will continue in the next row.

A ***padding*** of *10px* is used for the window, from the top and the two sides. And a ***margin*** of *5px* is used between each shape drawn.

Height and width are scaled by *2x* when drawn, so a rectangle initialzed as `Rectangle(2, 3)` will have a width of 4px and height of 6px when drawn, the same scaling applies to squares too.
