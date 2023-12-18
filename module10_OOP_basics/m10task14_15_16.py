"""
Implement class Contacts that will work with contacts. On the first stage we will add 
2 methods:
- list_contacts - returns list of contacts (variable contacts) form the current class instance
- add_contacts - adds new contact to list, that is defined in the object contacts

Class Contacts contains class variable current_id. It will be used for adding new contact as 
a unique contact identifier. When we add new contact following arguments should be passed to the add_contacts method:
name, phone, email, and favorite.
Method should create dictionary with keys and values of parameters:
example of the dictionary: 
{
    "id": 1,
    "name": "Wylie Pope",
    "phone": "(692) 802-2949",
    "email": "est@utquamvel.net",
    "favorite": True,
}
The dictionary should be added to contacts list. current_id should be incrimented after 
each add_contacts call.
#####################################################################################
#task15:

add get_contact_by_id(self, id) method that will search and retur a dictionary with the contact by it's id
###################################################################################33
#task16 
add remove_contacts(self, id) method that should delete a contact from the list by id.
If there is no contact no actions should be performed

"""

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts
        

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append({"id": Contacts.current_id,
                   "name": name,
                   "phone": phone,
                   "email": email,
                   "favorite": favorite
        })        
        Contacts.current_id += 1

#task15
    def get_contact_by_id(self, id):
        for contact in self.contacts:
            if contact["id"]==id:
                return contact
#enother implementation: 
#result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
#return result[0] if len(result) > 0 else None

#task16
    def  remove_contacts(self, id):
        self.contacts = list(filter(lambda contact: contact.get("id") !=id, self.contacts))

        

contacts_DB = Contacts()
contacts_DB.add_contacts("Serhii", "7293817", "serg@gmail.com", True)
contacts_DB.add_contacts("Kate", "11111", "kate@gmail.com", True)
contacts_DB.add_contacts("Dodik", "234232237", "dodik@gmail.com", False)

print("Show all list:")
print(contacts_DB.list_contacts())
print("Contact with id = 2:")
print(contacts_DB.get_contact_by_id(2))
contacts_DB.remove_contacts(3)
print("After remove 3-rd contact:")
print(contacts_DB.list_contacts())

            
                
                
                
                
                
            
        
        
