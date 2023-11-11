"""
1. Get list of phone numbers and normalize them
2. Sort them by country codes:
        UA: +380 or not present in list
        JP: +81 
        TW: +886
        SG: +65
3. Return dictionary in following format:
        {
            "UA": [<тут список телефонів>],
            "JP": [<тут список телефонів>],
            "TW": [<тут список телефонів>],
            "SG": [<тут список телефонів>]
        }
"""

def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    phones_dict = {"UA": [], "JP": [], "TW": [], "SG": []}
    print(phones_dict)
    ua_phones = []
    jp_phones = []
    tw_phones = []
    sg_phones = []   

    normalized_phone = None
    for phone in list_phones:
        normalized_phone = sanitize_phone_number(phone)
        if normalized_phone.startswith('81'):
            jp_phones.append(normalized_phone)
        elif normalized_phone.startswith('886'):
            tw_phones.append(normalized_phone)
        elif normalized_phone.startswith('65'):
            sg_phones.append(normalized_phone)
        else:
            ua_phones.append(normalized_phone)

    phones_dict["UA"] = ua_phones
    phones_dict["JP"] = jp_phones
    phones_dict["TW"] = tw_phones
    phones_dict["SG"] = sg_phones
    #phones_dict = phones_dict.update({'UA': ua_phones, 'JP': jp_phones, 'TW': tw_phones, 'SG': sg_phones})
    return phones_dict


phones = ['+380502590542', ' (886) 5342332', ' +81 50 234 45 45', '   65 2345 52 99', '099 4562343', '050 23452345',
          '+886 8983432']

print(get_phone_numbers_for_countries(phones))