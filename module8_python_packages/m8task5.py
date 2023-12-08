"""
get_random_winners(quantity, participants) should return 
winners of the lotery in the ammount of quantity.
participants is a following dictionary:
participants = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}
keys are unique identifier of MongoDB RDBMS

requirements:
1. get list of keys (after exec of keys() method use type conversion)
2. shuffle the list using method shuffle()
3. Select random winners using method sample()
4. if quantity is more than number of participants return the empty list

"""



import random


def get_random_winners(quantity, participants):
    if quantity> len(participants):
        return list()
    else:        
        candidates = list(participants.keys())
        random.shuffle(candidates)        
        return random.sample(candidates, k=quantity)
    


participants_dict = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}

print(get_random_winners(2, participants_dict))


