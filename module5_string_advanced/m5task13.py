
# (?:[a-zA-Z])+(?:[a-zA-Z]|_|\.|[0-9])+@[a-zA-Z]+\.[a-zA-Z]{2,}
"""
<find_all_emails> should search all emails in text
1. email should have only EN characters
2. before @ begins with a letter and can can contain any letter, number and underscore and point
3. after @ english letters and after "." can have more than 1 symbol

"""
import re


def find_all_emails(text):
    pattern = r"(?:[a-zA-Z])+(?:[a-zA-Z]|_|\.|[0-9])+@[a-zA-Z]+\.[a-zA-Z]{2,}"
    result = re.findall(pattern, text)
    return result


text ="sergey.kroshka@gmail.com and some sergey.kroshka.w@gmail.com + pm012@ukr.net this is not a email 1234@mail.ru neither this m@can.c, but this can be considered as email sergey_kroshka@mail.ua"
print(find_all_emails(text))

text1 =  'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net' 
print(find_all_emails(text1)) 
#  ['Ima.Fool@iana.org', 'Fool@iana.org', 'first_last@iana.org', 'first.middle.last@iana.or', 'abc111@test.com']