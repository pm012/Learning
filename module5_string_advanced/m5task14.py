"""
find number telephone of Ukraine in international standard
+380(xx)xxx-x(or xx)-xx (or xxx)
"""

#\+380\(\d{2,}\)\d{3}-\d{1}-\d{3}|\+380\(\d{2,}\)\d{3}-\d{2}-\d{2}

import re


def find_all_phones(text):
    pattern = r"\+380\(\d{2,}\)\d{3}-\d{1}-\d{3}|\+380\(\d{2,}\)\d{3}-\d{2}-\d{2}"
    result = re.findall(pattern, text)
    return result

text = "+380(50)456-4-345 +380(50)645-23-45 +545(23)123-54-66 +380965434545 +380(44)23-23-234"
print(find_all_phones(text))