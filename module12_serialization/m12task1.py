"""
In a list where each element is a dictionary as follows:
 {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

Develop 2 functions of serialization and deserialization of contacts list with the help of package 
pickle and save the data in a binary file.

<write_contacts_to_file> takes 2 parameters: filename - the name of a file and contacts - list of conacts
It saves the list in a file using method dump of pickle package.

<read_contacts_from_file(filename) reads and returns the list of contacts from <filename> using method load of 
package pickle

"""

import pickle
import faker


def write_contacts_to_file(filename, contacts):
    with open (filename, 'wb') as fn:
        pickle.dump(contacts, fn)

    
        


def read_contacts_from_file(filename):
    with open(filename, 'rb') as fn:
        return pickle.load(fn)
        


if __name__ == "__main__":
    file_path = "./module12_serialization/ser_files/contacts.txt"


    fake = faker.Faker()

    # Generate a list of 8 dictionaries
    contact_list = [
        {
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "favorite": fake.boolean(),
        }
        for _ in range(8)
    ]

    # # Print the list of dictionaries
    # for contact in contact_list:
    #     print(contact)

write_contacts_to_file(file_path, contact_list)
print(read_contacts_from_file(file_path))
