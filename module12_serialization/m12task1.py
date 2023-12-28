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


def write_contacts_to_file(filename, contacts):
    with open (filename) as fn:
        text = "\n".join(contacts)

    
        


def read_contacts_from_file(filename):
    pass
        
    
