# Access libraries and py files 
import spiderDraw as sd
import functions as md

# Print intro statements (welcome to game, etc)
md.introduction()

# Initialize variables and setup 
correct = []  # List of correct letters guessed
incorrect = []  # List of incorrect letters guessed
tries = 0   # Number of incorrect guesses
game = True 

# Make a list of the spider drawings
spiderList = [sd.spider_0, sd.spider_1, sd.spider_2, sd.spider_3, sd.spider_4, sd.spider_5, sd.spider_6]

# Generate a random word from word list
word = md.generate_word()  

# Game Loop
while game: 
    print(md.print_word(word, correct))
    md.print_wrong_guesses(incorrect)
    md.print_spider(tries, spiderList)
    
    guess = input('Guess a letter\n').lower()
    
    if not md.is_guess_valid(guess):
        print('Please input only one letter\n')
        continue

    if md.already_guessed(guess, correct, incorrect):
        print("You already guessed that letter.\n")
        continue

    tries = md.check_word(guess, correct, incorrect, word, tries)

    if all(letter in correct for letter in word):
        print(f"\nYou won! The word was '{word}'.")
        game = False
    elif tries >= 6:
        md.print_spider(tries, spiderList)
        print(f"\nGame over! The word was '{word}'.")
        game = False
