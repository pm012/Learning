"""Do the serialization and deserialization using csv file. The structure of csv"""
import faker
import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as fn:
        field_names = contacts[0].keys()
        writer = csv.DictWriter(fn, fieldnames=field_names)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)


def read_contacts_from_file(filename):
    result = list()
    with open(filename, newline='') as fn:        
        reader = csv.DictReader(fn)
        for row in reader:
            result.append({
                'name':row['name'],
                'email': row['email'],
                'phone': row['phone'],
                'favorite': eval(row['favorite']) 
            })            
    return result

if __name__ == "__main__":
    file_path = "./module12_serialization/ser_files/contacts.csv"


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
#write dictionary to csv without csv methods usage:
    # print(", ".join(contact_list[0].keys()))
    # for contact in contact_list:
    #     #print(", ".join(list(contact.values())))
    #     print(", ".join(str(value) for value in contact.values()))

    # write_contacts_to_file(file_path, contact_list)
    # print(contact_list)
    # print('_______________')
    # print(read_contacts_from_file(file_path))

    print(eval('False'))