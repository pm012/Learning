"""
Create child class Cat with parent Animal. 
Redefine method <say> in Cat, to return string "Meow" for 
object of class Cat

Create object cat of class Cat with name Simon and weight =10


task6: add class Dog that will be a child of class Animal and redefine method say to return "Woof" and add object attribute breed

"""

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"
    
class Dog(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed=breed
    
    def say(self):
        return "Woof"


dog = Dog("Barbos", 23, "labrador")

    
cat = Cat("Simon", 10)

