from random import choice

hangman_pics = [
    """
      +---+
          |
          |
          |
         ===""",
    """
      +---+
      O   |
          |
          |
         ===""",
    """
      +---+
      O   |
      |   |
          |
         ===""",
    """
      +---+
      O   |
     /|   |
          |
         ===""",
    """
      +---+
      O   |
     /|\  |
          |
         ===""",
    """
      +---+
      O   |
     /|\  |
     /    |
         ===""",
    """
      +---+
      O   |
     /|\  |
     / \  |
         ==="""
]

words = ['python', 'poker', 'programing', 'sunflower', 'Ukraine']

word = choice(words).upper()

guessed = list()

def print_word():
    display_word = ""
    for char in word:
        display_word += str(char if char in guessed else "_")
    print(display_word)
    return display_word

def main():
    attempts = 6
    while attempts > 0:
        print(hangman_pics[6 - attempts])
        display_word = print_word()

        if "_" not in display_word:
            print(f"Congratulations! You win this game and still alive. The guessed word was {word}")
            break

        guess = input("Guess a letter: ").upper()

        if guess in guessed:
            print("You already guessed this letter")
        elif guess in word:
            print("Correct guess!")
            guessed.append(guess)
        else:
            print("Wrong guess!")
            attempts -= 1
            guessed.append(guess)

    if attempts == 0:
        print(hangman_pics[-1])
        print(f"You ran out of attempts. The word was: {word}")

if __name__ == '__main__':
    main()