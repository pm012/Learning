"""s - spades
h - hearts
d - diamonds
C - clovers


"""
from random import randrange


def create_deck():
    deck=[]
    suits = ["s","h","d","c"]
    values = ['2', '3', '4', '5','6','7','8', '9', '10', 'J', 'Q', 'K', 'A']
    for suit in suits:
        for value in values:
            deck.append(suit+value)

    return deck
        
#print(create_deck())





#TODO rebuild function using more enhanced choice  or sample: choice(list), sample(list, len(list))
def shuffle_deck(deck):
    new_deck = deck.copy()
    for i in range(0, len(deck)):
        other_index = randrange(0, len(new_deck))
        new_deck[i], new_deck[other_index] = new_deck[other_index], new_deck[i]
    return new_deck


def deal(players, cards, deck):
    if players * cards > len(deck):
        return deck

    table = list()
    for _ in range(0, cards):
        for player in range(players):
            if player >= len(table):
                table.append([deck.pop()])
            else:
                table[player].append(deck.pop())

    return table

#print(deal(4, 6, create_deck()))


#game imitation
def main(players, cards):
    init_deck = create_deck()
    print(f"Open new deck: {init_deck}")

    deck = shuffle_deck(init_deck)
    print(f" shuffled deck: {deck}")
    print(f"Invite {players} players to table")
    print (f"Give {cards} cards to each players")

    table = deal(players, cards, deck)

    for i in range(players):
        print(f"Player number {i+1} has cards: {table[i]}")

    print(f"Deck in the final: {deck}")

if __name__== '__main__':
    main(4,6)



