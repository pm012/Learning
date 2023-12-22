"""
Create class Point which will reflect geometric point on the surface.

Implement via constructor initialization of 2 attributes: coordinate x and coordinate y.


"""

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y


point = Point(5, 10)
print(point.x)
print("___________________")
print(point.y)