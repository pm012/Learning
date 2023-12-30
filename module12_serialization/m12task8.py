""""
for Contacts class implement function copy_class_contacts. It takes instance of Contacts as a parameter and returns deep copy
of object with the help of function deepcopy of package copy
"""
import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True


def copy_class_contacts(contacts):
    return copy.deepcopy(contacts)


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
    persons = Contacts("user_class.dat", contacts)

    new_persons = copy_class_contacts(persons)

    new_persons.contacts[0].name = "Another name"

    print(persons.contacts[0].name)  # Allen Raymond
    print(new_persons.contacts[0].name)  # Another name

