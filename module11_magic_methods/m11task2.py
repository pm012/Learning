"""
Create class Point which will reflect geometric point on the surface.

Implement via constructor initialization of 2 attributes: coordinate x and coordinate y.
Hide access to x, y using __x and __y
Implement setter and getter for attributes __x and __y with the help of decorators property and setter


"""

class Point:
    def __init__(self, x, y):
        self.__x = x 
        self.__y = y

    @property
    def x(self):
        return self.__x
    @property 
    def y(self):
        return self.__y
    
    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @y.setter
    def y(self, new_y):
        self.__y = new_y


point = Point(5, 10)
print(point.x)
print("___________________")
print(point.y)