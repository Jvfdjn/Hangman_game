import random

# Importing the hangman_logo from a separate module named 'logo'
from logo import hangman_logo

# Printing the hangman_logo
print(hangman_logo)

# List of hangman pictures for different stages of the game
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Initializing lives to -7 (Note: it's usually more common to start with 0 or a positive value)
lives = -7

# Importing the list of hangman words from a separate module named 'hangman_words'
from hangman_words import hangman_words

# Creating a tuple with the imported hangman_words
words = tuple(hangman_words)

# Choosing a random word from the list and converting it to lowercase
chosen_word = random.choice(words).lower()
print(chosen_word)

# Initializing the display list to store guessed letters
display = []

# Getting the length of the chosen word
word_length = len(chosen_word)

# Initializing the display list with underscores for each letter in the chosen word
for letters in chosen_word:
    display += "_"
print(display)

# Flag to control the game loop
end_of_game = False

# Main game loop
while not end_of_game:
    # Getting a letter guess from the user and converting it to lowercase
    guess = input("Guess a letter: ").lower()

    # Checking if the guessed letter is in the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If the guessed letter is not in the chosen word, decrement lives
    if guess not in chosen_word:
        lives += 1

        # If lives reach 0, end the game and print "you lose"
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Printing the current state of the display
    print(display)

    # If there are no underscores left in the display, end the game and print "You win"
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Printing the hangman picture corresponding to the current number of lives
    print(HANGMANPICS[lives])
