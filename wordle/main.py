#Wordle Clone Outline
#Follow comments to help build out your game

import random
#Set Up Game Variables. We will need variables to:
#store the number of guesses the player has made
#store the different colors we want to use
#keep track of letters that were guessed in the correct position
#letters guessed that were in the incorrect position 
#letters guessed that were not in the word at all.

GREEN = '\033[42m\033[30m'  
YELLOW = '\033[43m\033[30m' 
GRAY = '\033[47m\033[30m'    
RESET = '\033[0m'

correct_letters = []
wrong_place_letters = []
wrong_letters = []
Attempts = 1

#Create your Welcome message that explains how the game works

print("Welcome to Wordle!!")
print("Try to guess the 5 letter word in 5 tries")
print("Green = correct letter & correct position")
print("Yellow = correct letter, wrong position")
print("Gray = not in the word at all\n")
print("Good Luck!!!!!!!!!!")

def load_word_list():
    with open("word_list.txt", "r") as f:
        return [line.strip().lower() for line in f if len(line.strip()) == 5]

#Generate Word Function. Opens a word list file, then chooses a word at random
def generate_word(word_list):
    return random.choice(word_list)

#Get User Guess Function. Prompts user for a guess, checks to make sure it is a 5 letter word

def get_guess(word_list):
    while True:
        guess = input("Enter your guess: ").lower()
        if len(guess) != 5:
            print("Guess must be 5 letters")
        if guess not in word_list:
            print("Your guess is not in the word list")
            get_guess()


#Compare Words Function. Compares the word guessed by the player to the solution word generated at random earlier. Needs to check if each letter of the guess is in the solution word, and if so, if it is in the correct position or not. Then it will print out the guess word again, with each letter colored to reflect whether it was wrong, correct letter but wrong position, or completely correct.

def compare_words(guess, secret):
    result = ""
    for i in range(5):
        letter = guess[i]
        if letter == secret[i]:
            result += GREEN + " " + letter.upper() + " " + RESET
            if letter not in correct_letters:
                correct_letters.append(letter)
        elif letter in secret:
            result += YELLOW + " " + letter.upper() + " " + RESET
            if letter not in wrong_place_letters:
                wrong_place_letters.append(letter)
        else:
            result += GRAY + " " + letter.upper() + " " + RESET
            if letter not in wrong_letters:
                wrong_letters.append(letter)
    print(result)


#Print Letters Function - Prints the entire alphabet for the user, coloring all letters that have been guessed so far to reflect if those letters were 1. Not in the word at all, 2. In the word but wrong position or 3. In the word and correct position

def print_letters():
    print("Correct (Green):     ", " ".join(correct_letters))
    print("Wrong Spot (Yellow): ", " ".join(wrong_place_letters))
    print("Not in Word (Gray):  ", " ".join(wrong_letters))
    print()

#Game Loop. Calls the functions. Checks for win or lose conditions. Wins if all letters are in the correct place and there are less than 5 guesses. 

def play_game():
    word_list = load_word_list()
    secret_word = generate_word(word_list)
    attempts = 0
    max_attempts = 6

    while attempts < max_attempts:
        print("Attempt", Attempts)
        print_letters()
        guess = get_guess(word_list)
        compare_words(guess, secret_word)
        if guess == secret_word:
            print(" You guessed the word!")
            break
        attempts += 1
    else:
        print("You're out of tries. The word was: {secret_word.upper()}")

play_game()