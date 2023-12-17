#tasks 1-4

class Animal:
    #class wariable, should be changed for all objects
    color = "white"

    def __init__(self, nickname, weight) -> None:        
        self.nickname = nickname
        self.weight = weight

    def say():
        pass


    def change_weight(self, new_weighgt):
        # Object variable, changed for object that calls the method        
        self.weight = new_weighgt

    def change_color(self, new_color):
        Animal.color = new_color

first_animal=Animal("Siam",5)
second_animal = Animal("Yasha",6)
second_animal.change_color("red")


print(first_animal.color)




animal = Animal("Borka", 50)
animal.change_weight(12)
