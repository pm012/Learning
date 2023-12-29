"""
serialize and deserialize file using json (javascript object notation protocol)

"""
import faker
import json


def write_contacts_to_file(filename, contacts):
    with open (filename, 'w') as fn:
        json_structure = {"contacts": contacts}
        json.dump(json_structure, fn)

    
        


def read_contacts_from_file(filename):
    with open(filename, 'r') as fn:
        list = json.load(fn)["contacts"]
        return list
    

if __name__ == "__main__":
    file_path = "./module12_serialization/ser_files/contacts.json"


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
