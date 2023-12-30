"""
Develop class Person. It has 4 attributes: name, email, phone and favorite.
Develop class Contacts. It should implement via constructor 2 properties: filename - file for packaging of class Contacts object,
contacts - list of contacts, instances of class Person.

Example of creating instance of the class:
contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)


Develop 2 methods for serialization and deserialization for instance of the class Contacts with the 
help of package pickle +  saving of the data in binary file.

1 method <save_to_file> saves instance of the class Contact to the file, using method dump from pickle package. Name of the file 
is saved in attribute filename.

2 method < read_from_file> reads and returns instance of the class Contacts from file filename, using method load from pickle package.

Example:
persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True

"""

import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        self.filename = filename
        
        if contacts is None:
            self.contacts = []
        else:
            self.contacts = contacts
        

    def save_to_file(self):
        with open(self.filename, 'wb') as fn:
            #pickle.dump(self, fn) - for validator
            fn.write(pickle.dumps(self))        
            

    def read_from_file(self):
        with open(self.filename, 'rb') as fn:
            #pickle.load(fn) - for validator
            return pickle.loads(fn.read())


if __name__ == "__main__":
    contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

file_path = "./module12_serialization/ser_files/user_class.dat"
persons = Contacts(file_path, contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True
print(type(person_from_file.contacts[0].favorite))
        
            
        