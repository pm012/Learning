"""
Based on previous task.
to the properties x, y setter add additional validation:
It is allowed to add x or y if they are of (int) or (float) type

"""
ALLOWED_TYPES = ("int", "float")
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
        if type(x).__name__ in  ALLOWED_TYPES:
            self.__x=x

        
            

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y).__name__ in  ALLOWED_TYPES:
            self.__y=y


point = Point("a", 10)

print(point.x)
print(point.y)