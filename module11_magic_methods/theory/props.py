class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age
    

    def set_age(self, age):
        self.__age = age

    age = property(get_age, set_age)


person = Person('Serhii', '32')
person.__dict__['age'] = 'old'
print(person.age, person.__dict__)
person.age = 44
print(person.age, person.__dict__)
    
