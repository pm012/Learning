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
        copy_obj = Person(copy.copy(self.name), 
                          copy.copy(self.email), 
                          copy.copy(self.phone),
                          copy.copy(self.favorite))        
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
        copy_obj = Contacts(copy.copy(self.filename),
                            copy.copy(self.contacts))
        copy_obj.is_unpacking = copy.copy(self.is_unpacking)
        copy_obj.count_save = copy.copy(self.count_save)
        
        return copy_obj       
        

    def __deepcopy__(self, memo):
        copy_obj = Contacts(copy.deepcopy(self.filename), copy.deepcopy(self.contacts))
        memo[id(copy_obj)] = copy_obj        
        copy_obj.is_unpacking = copy.copy(self.is_unpacking)
        copy_obj.count_save = copy.copy(self.count_save)       
        return copy_obj
    

if __name__ == "__main__":
      # Example usage
    original_person = Person("John", "john@example.com", "123456", True)

    # Create a shallow copy
    copied_person = copy.copy(original_person)

    # Check if the copy is independent of the original
    print(original_person.name)  # Output: John
    print(copied_person.name)    # Output: John

    # Modify the original
    original_person.name = "Jane"

    # Check if the copy remains unchanged
    print(original_person.name)  # Output: Jane
    print(copied_person.name)    # Output: John
