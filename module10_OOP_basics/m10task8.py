"""
Create 2 classes: CatDog and DogCat. These classes should extend both Cat and Dog.
After inheritance parent method of CatDog say should return "Meow" and for DogCat should return "Woof"
for both classes implement method <info>, that should return string in following format: f"{self.nickname}-{self.weight}"
"""


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"

class CatDog(Cat, Dog):
    def info(self):
        return f"{self.nickname}-{self.weight}"
    

class DogCat(Dog, Cat):
    def info(self):
        return f"{self.nickname}-{self.weight}"
    


catdog = CatDog("Siam",10)
dog_cat = DogCat("Barsik", 15)
print(catdog.say())
print(dog_cat.say())

print(catdog.info())
print(dog_cat.info())
    
        


    
        