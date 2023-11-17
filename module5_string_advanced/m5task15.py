"""
The find_all_links function should extract all matched URLs from <text>.
* Beginning of the link can be http:// or https://
* Domain name is set of lathin letters, numbers, underscore symbols '_' and periods '.'
* Periods cannot be located one by another

"""

import re


def find_all_links(text):
    pattern = "https?:\/\/{1}[a-zA-Z0-9_.]+"
    result = []
    iterator = re.finditer(pattern, text)
    for match in iterator:
        if ".." not in match.group():
               result.append(match.group())
    return result


text = "https://www.google.com https://www.facebook.com gmail.com https://github.com https://rest..ua.com, https://can_ua.com"
urls_list = find_all_links(text)
print(urls_list)