"""
For class Dog implement attribute onwer that is an object of Owner class.
Add <who_is_owner> to Dog class that will return result of method <info> call - it's a dictionary with keys name, age and address.

"""

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address ):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return vars(self)
        


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()
    



owner = Owner("Name", 20, "Dnipro, Yavornitskogo st., 34")
dog = Dog("Woolf", 20, "hasky", owner)
print(dog.who_is_owner())