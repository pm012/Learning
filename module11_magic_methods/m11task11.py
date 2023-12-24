"""
Implement RandomVectors, that can create object, that can be iterated and allow iterate on random vectors.

Fromat of the class:
RandomVectors(max_vectors: int, max_points: int) -> Iterable(max_vectors, max_points)

where
- max_vectors - defines maximal number of elements in iterable sequence
- max_points - defines maximal value for coordinates x and y ( in range 0..max_points)

It should be implemented method __iter__ that will return iterator.
Iterator - is any object, that on each step of iteration (step of iteration is call of next() for the iterator) returns value and so on till the last iteration 
(defined by parameter max_vectors)

In our case iterator is a class Iterable, in which it is required to implement method __next__. In constuctor the class gets the same parameters
max_vecors and max_points as RandomVectors class.

Method __next__ should return each next value from the list self.vectors. Create in a constructor set of random vectors self.vectors with lenght max_vectors with
help of randrange. Attribute current_index is a pointer-index to the current vector from the list vectors, needed for iterating.

For example:
vectors = RandomVectors(5, 10)

for vector in vectors:
    print(vector)

Will output:
Vector(7,7)
Vector(0,0)
Vector(8,9)
Vector(1,9)
Vector(6,6)

In short:
1. RandomVectors should have method __iter__, that will return iterator object (class Iterable)
2. The object of Iterable should have method __next__
3. Method __next__  should control number of possible steps of iteration and will be defined by max_vectors parameter
4. If we exhausted all possible steps __next__ should generate exception StopIteration
5. Else method __next__ returns vector with random coordinates (instance of class Vector). Size of coordinates of vector is defined by parameter max_points.



"""



from random import randrange


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
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        return (
                self.coordinates.x * vector.coordinates.x
                + self.coordinates.y * vector.coordinates.y
        )

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

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


class Iterable:
    def __init__(self, max_vectors, max_points):
        self.current_index = 0
        self.vectors = []
        self.max_vecors = max_vectors
        self.max_points = max_points       
            

    def __next__(self):
        if self.current_index < self.max_vecors:
            self.current_index +=1
            x = randrange(0, self.max_points)
            y = randrange(0, self.max_points)
            point = Point(x, y)
            return Vector(point)
        raise StopIteration 
            


class RandomVectors:
    def __init__(self, max_vectors=10, max_points=50):
        self.max_vecors = max_vectors
        self.max_points = max_points
        
        

    def __iter__(self):
        return Iterable(self.max_vecors, self.max_points)
        


vectors = RandomVectors(5, 10)

for vector in vectors:
    print(vector)