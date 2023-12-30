"""
For copying of class Person from the previous example implement function copy_class_person.
It gets instance of a class person as a parameter and returns copy of the object
with help of function copy (package copy)

"""
import copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)


if __name__ == "__main__":
    person = Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    )

    copy_person = copy_class_person(person)

    print(copy_person == person)  # False
    print(copy_person.name == person.name)  # True