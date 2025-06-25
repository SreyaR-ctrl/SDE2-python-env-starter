import random

# Returns the word to the console containing "_" for any letter not guessed by the user.
# Takes in the correct word and the list of correct guesses as parameters
def print_word(word, correct):
    return ' '.join([letter if letter in correct else '_' for letter in word])

# Displays a list of wrong guesses
def print_wrong_guesses(incorrect):
    print("Wrong guesses:", ' '.join(incorrect))

# Prints spider from the spider drawing functions in the spiderDraw.py file.
# Takes the number of wrong guesses and the list of spider drawing functions as parameters.
def print_spider(tries, spiderList):
    spiderList[tries]()

# Opens the word list file, picks a random word, and prints blanks
def generate_word():
    wordList = open('Lesson6/aracnophonics1/words.txt').read().split()
    word = random.choice(wordList).lower()
    print('Word = ' + '_' * len(word))
    return word

# Checks if guess was already made
def already_guessed(guess, correct, incorrect):
    return guess in correct or guess in incorrect

# Checks the guess, updates lists, prints result; returns updated tries
def check_word(guess, correct, incorrect, word, tries):
    if guess in correct or guess in incorrect:
        print("You already guessed that letter.")
    elif guess in word:
        correct.append(guess)
        print("Correct!")
    else:
        incorrect.append(guess)
        tries += 1
        print("Incorrect.")
    return tries

# Greets the user and starts the game
def introduction():
    name = input("Welcome to Arachnophonics! What's your name? ")
    print(f"Hi {name}!\n")

# Checks if guess is in the word
def is_guess_correct(guess, word):
    return guess.lower() in word

# Validates that guess is a single alphabetical character
def is_guess_valid(guess):
    return guess.isalpha() and len(guess) == 1