"""
Based on previous task
For instance of class Vector implement functor. Create for the class method __call__
it should return tuple with vector coordinates if it is called as a function e.g.:
vector = Vector(Point(1, 10))

print(vector())  # (1, 10)

if a number is passed as a parameter it should return tuple with coordinates multiplied on that number:
vector = Vector(Point(1, 10))

print(vector(5))  # (5, 50)



"""
class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value is None:
            return self.coordinates.x, self.coordinates.y
        elif type(value).__name__ == "int":
            return self.coordinates.x*value, self.coordinates.y*value
        
            
            
        

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"
    

vector = Vector(Point(1, 10))

print(vector())  # (1, 10)

vector = Vector(Point(1, 10))

print(vector(5))  # (5, 50)