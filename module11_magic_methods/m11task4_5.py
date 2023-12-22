"""
Implement class Vector. Property coordinates should define coordinates of the vector and is an instance
of the class Point. Start of the vector is in the point (0,0) and end of the vector will be defined by 
coordinates attribute.

Implement ability to call vector Vector coordinates using square brackets:
vector = Vector(Point(1, 10))

print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10

vector[0] = 10  # Встановлюємо координату x вектора 10

print(vector[0])  # 10
print(vector[1])  # 10

To get value of object print(vector[0]) using square brackets, implement method __getitem__ in the class Vector.

For setting coordinates of vector via index (as vector[0] = 10), implement method __setitem__ in class Vector.

Reference to coordinate x is done using index 0, and y - using index 1

task5:
Implement magic method __str__
for Point class to output Point(<x>,<y>)
for Vector class to output Vector(<x>,<y>)

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
        match index:
            case 0:
                self.coordinates.x = value
            case 1:
                self.coordinates.y = value
            case _:
                raise ValueError("Index should be in [0,1]")            

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise ValueError("Index should be in [0,1]")
        
    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"
        

        
            
        
vector = Vector(Point(1, 10))

print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10
point = Point(3, 4)
print(point)

vector[0] = 10  # Set coordinate x of vector to be 10

print(vector[0])  # 10
print(vector[1])  # 10
print(vector)