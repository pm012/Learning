"""
filter contacts list, elements of which are dictionaries in following format:
 {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
function <get_favorites(contacts) should return list that contain only selected contacts. 
Use function filter

"""
def get_favorites(contacts):
    contacts_res = list()
    for i in filter(lambda x: x['favorite'], contacts):
        contacts_res.append(i)

    return contacts_res

contacts_list= [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},
{
    "name": "Allen Delon",
    "email": "allen.delon@vestibul.co.uk",
    "phone": "(992) 344-6331",
    "favorite": True,
},
{
    "name": "Gilian Anderson",
    "email": "gilla.andersen@vestibul.co.uk",
    "phone": "(991) 444-6233",
    "favorite": True,
},
{
    "name": "Raymond Pauls",
    "email": "raymond.pauls@vestibul.co.uk",
    "phone": "(992) 334-34523",
    "favorite": False,
} ]

print(get_favorites(contacts_list))

