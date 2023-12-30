"""
Add to Contacts class attribute is_unpacking (by default = False).
Implement method __setstate__ for the class Contacts.
During extracting instanse of the class method should change is_unpacking to True.

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
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0
        self.is_unpacking = False
        

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] +=  1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

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

file_path = "./module12_serialization/ser_files/user_class_task6.dat"
persons = Contacts(file_path, contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons.is_unpacking)  # False
print(person_from_file.is_unpacking)  # True
        