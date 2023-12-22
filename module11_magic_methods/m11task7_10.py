"""
Implement for Vector class operations of addition and substitution of vectors (__add__, __sub__).
vector one: a with coordinatest(x1, y1)
vector two: b with coordinates (x2, y2)
b+a = (x2+x1, y2+y1)
b-a = (x2-x1, y2-y1)

###
task8
implement multiplication of 2 vectors __mul__

b*a = x2*x1 + y2*y1
###
task9
implement method len() to calculate length of the vector. For len(vector1) = (x1**2 + y1**2)**0.5
###
task10
implement and define all comparison methods for vectors based on method len



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
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x,y))
        

    def __sub__(self, vector):
        point = Point(self.coordinates.x - vector.coordinates.x, self.coordinates.y - vector.coordinates.y)
        return Vector(point)
    
    # Task8
    def __mul__(self, vector):
        return self.coordinates.x * vector.coordinates.x + self.coordinates.y * vector.coordinates.y
    # Task 9
    def len(self):
        return (self.coordinates.x**2 + self.coordinates.y**2)**0.5
    
    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"
    
    # Task 10
    def __eq__(self, vector):
        return self.len() == vector.len()
        

    def __ne__(self, vector):
        return self.len() != vector.len()
        

    def __lt__(self, vector):
        return self.len() < vector.len()
        

    def __gt__(self, vector):
        return self.len() > vector.len()
        

    def __le__(self, vector):
        return self.len() <= vector.len()
        

    def __ge__(self, vector):
        return self.len() >= vector.len()
    



# Sample of code
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

scalar = vector1 * vector2
vector3 = vector2 + vector1
vector4 = vector2 - vector1

print(vector3)  # Vector(11,20)
print(vector4)  # Vector(9,0)
print(scalar) #110
print(vector1.len())

#task 10 testing
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(3, 10))

print(vector1 == vector2)  # False
print(vector1 != vector2)  # True
print(vector1 > vector2)  # False
print(vector1 < vector2)  # True
print(vector1 >= vector2)  # False
print(vector1 <= vector2)  # True
