from collections import UserDict
from random import randint

class Card(UserDict):
    number_per_letter = 15
    limit_line  = 5
    loto_field = ['B', 'I', 'N', 'G', 'O']


    def __init__(self):
        super().__init__()
        self.min_num = 1
        self.max_num = self.number_per_letter
        self.create_card()


    def create_card(self):
        for letter in self.loto_field:
            self.data[letter] = []
            while len(self.data[letter]) < self.limit_line:
                next_num = randint(self.min_num, self.max_num)
                if next_num not in self.data[letter]:
                    self.data[letter].append(next_num)
            self.min_num = self.max_num + 1
            self.max = self.max_num + self.number_per_letter

    def pretty_card_info(self):
        print('{:^5}{:^5}{:^5}{:^5}{:^5}'.format(*self.data))
        for i in range(self.limit_line):
            line = list()
            for letter in self.loto_field:
                line.append(self.data[letter][i])
            print('{:^5}{:^5}{:^5}{:^5}{:^5}'.format(*line))
            line.clear()
        

card = Card()
card.pretty_card_info()