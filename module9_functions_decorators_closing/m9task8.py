"""
List of contacts, that contains dictionary in following format:
{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

Implement get_emails function that recives list_contacts list as a parameter and returns list
that contain emails of all contacts from <list_contacts>. Use map function

"""

def get_emails(list_contacts):
    emails_list=list()
    for i in map(lambda x: x['email'], list_contacts):
        emails_list.append(i)

    return emails_list


contacts = [
    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False},
    {
    "name": "Allen Raymond",
    "email": "sharlotte.bronte@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False},
    {
    "name": "Allen Raymond",
    "email": "monserat.cabaliery@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False}
    ]

print(get_emails(contacts))