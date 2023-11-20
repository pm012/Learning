"""encode_data_to_base64 gets list of users and passwords from the previous task
and returns with base64 encrypted data
eg. input:
['andry:uyro18890D', 'steve:oppjM13LL9e']

output:
['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']
 """

import base64


def encode_data_to_base64(data):
    res = []
    tmp = None
    for record in data:
        tmp = base64.b64encode(record.encode('utf-8')) #encode string to utf-8 and then to base64
        res.append(tmp.decode("utf-8")) # decoted encrypted in base64 string to utf-8

    return res


usr_lst = ['andry:uyro18890D', 'steve:oppjM13LL9e']

print(encode_data_to_base64(usr_lst))