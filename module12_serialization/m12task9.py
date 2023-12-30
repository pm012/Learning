"""
Implement method __copy__ for class Person.
Implement method __deepcopy__ and __copy__ for class Contacts.
"""
import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        copy_obj = Person(
            copy.copy(self.name),
            copy.copy(self.email),
            copy.copy(self.phone),
            copy.copy(self.favorite)
        )
        return copy_obj


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

    def __copy__(self):
        copy_obj = self
        copy_obj.filename = copy.copy(self.filename)
        copy_obj.contacts = copy.copy(self.contacts)
        copy_obj.is_unpacking = copy.copy(self.is_unpacking)
        copy_obj.count_save = copy.copy(self.count_save)
        return copy_obj       
        

    def __deepcopy__(self, memo):
        copy_obj = self
        memo[id(copy_obj)] = copy_obj
        copy_obj.filename = copy.deepcopy(self.filename)
        copy_obj.contacts = copy.deepcopy(self.contacts)
        copy_obj.is_unpacking = copy.copy(self.is_unpacking)
        copy_obj.count_save = copy.copy(self.count_save)       
        return copy_obj
    

if __name__ == "__main__":
      person = Person(
                "Allen Raymond",
                "nulla.ante@vestibul.co.uk",
                "(992) 914-3792",
                False,
                )
      
      person_copy = copy.copy(person)

      print(person == person_copy)
      print(person is person_copy)
