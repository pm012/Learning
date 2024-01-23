from datetime import datetime

test = datetime.now()
test2 = '1234567'
test3 = [1,2,3]


print(str(test))
print(repr(test))

print(str(test2))
print(repr(test2))


print(str(test3))
print(repr(test3))

#=================================================

class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __str__(self):
        return f'{self.real} + i{self.image}'
    
    def __repr__(self) -> str:
        return f'{self.real} - i{self.image}'
    
    
number = Complex(10, 20)
print(number)
print(str(number))
print(repr(number))


