"""
return only positive numbers from the list using filter function


"""

def positive_values(list_payment):
    positive_result = list()
    for i in filter(lambda x: x>0, list_payment):
        positive_result.append(i)

    return positive_result


payment = [100, -3, 400, 35, -100]

print(positive_values(payment))