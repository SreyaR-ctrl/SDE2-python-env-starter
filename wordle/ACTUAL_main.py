#Wordle Clone Outline
#Follow comments to help build out your game
import random

#i physically could not get it to work with work_list.txt
# i have the one that tried to do that but also i made this .py file with a list instead
words = [
    "which", "there", "their", "about", "would", "these", "other", "words", "could", "write",
    "first", "water", "after", "where", "right", "think", "three", "years", "place", "sound",
    "great", "again", "still", "every", "small", "found", "those", "never", "under", "might",
    "while", "house", "world", "below", "asked", "going", "large", "until", "along", "shall",
    "being", "often", "earth", "began", "since", "study", "night", "light", "above", "paper",
    "parts", "young", "story", "point", "times", "heard", "whole", "white", "given", "means",
    "music", "miles", "thing", "today", "later", "using", "money", "lines", "order", "group",
    "among", "learn", "known", "space", "table", "early", "trees", "short", "hands", "state",
    "black", "shown", "stood", "front", "voice", "kinds", "makes", "comes", "close", "power",
    "lived", "vowel", "taken", "built", "heart", "ready", "quite", "class", "bring", "round",
    "horse", "shows", "piece", "green", "stand", "birds", "start", "river", "tried", "least",
    "field", "whose", "girls", "leave", "added", "color", "third", "hours", "moved", "plant",
    "doing", "names", "forms", "heavy", "ideas", "cried", "check", "floor", "begin", "woman",
    "alone", "plane", "spell", "watch", "carry", "wrote", "clear", "named", "books", "child",
    "glass", "human", "takes", "party", "build", "seems", "blood", "sides", "seven", "mouth",
    "solve", "north", "value", "death", "maybe", "happy", "tells", "gives", "looks", "shape",
    "lives", "steps", "areas", "sense", "speak", "force", "ocean", "speed", "women", "metal",
    "south", "grass", "scale", "cells", "lower", "sleep", "wrong", "pages", "ships", "needs",
    "rocks", "eight", "major", "level", "total", "ahead", "reach", "stars", "store", "sight",
    "terms", "catch", "works", "board", "cover", "songs", "equal", "stone", "waves", "guess",
    "dance", "spoke", "break", "cause", "radio", "weeks", "lands", "basic", "liked", "trade",
    "fresh", "final", "fight", "meant", "drive", "spent", "local", "waxes", "knows", "train",
    "bread", "homes", "teeth", "coast", "thick", "brown", "clean", "quiet", "sugar", "facts",
    "steel", "forth", "rules", "notes", "units", "peace", "month", "verbs", "seeds", "helps",
    "sharp", "visit", "woods", "chief", "walls", "cross", "wings", "grown", "cases", "foods",
    "crops", "fruit", "stick", "wants", "stage", "sheep", "nouns", "plain", "drink", "bones",
    "apart", "turns", "moves", "touch", "angle", "based", "range", "marks", "tired", "older",
    "farms", "spend", "shoes", "goods", "chair", "twice", "cents", "empty", "alike", "style",
    "broke", "pairs", "count", "enjoy", "score", "shore", "roots", "paint", "heads", "shook",
    "serve", "angry", "crowd", "wheel", "quick", "dress", "share", "alive", "noise", "solid",
    "cloth", "signs", "hills", "types", "drawn", "worth", "truck", "piano", "upper", "loved",
    "usual", "faces", "drove", "cabin", "boats", "towns", "proud", "court", "model", "prime",
    "fifty", "plans", "yards", "prove", "tools", "price", "sheet", "smell", "boxes", "raise",
    "match", "truth", "roads", "threw", "enemy", "lunch", "chart", "scene", "graph", "doubt",
    "guide", "winds", "block", "grain", "smoke", "mixed", "games", "wagon", "sweet", "topic",
    "extra", "plate", "title", "knife", "fence", "falls", "cloud", "wheat", "plays", "enter",
    "broad", "steam", "atoms", "press", "lying", "basis", "clock", "taste", "grows", "thank",
    "storm", "agree", "brain", "track", "smile", "funny", "beach", "stock", "hurry", "saved",
    "sorry", "giant", "trail", "offer", "ought", "rough", "daily", "avoid", "keeps", "throw",
    "allow", "cream", "laugh", "edges", "teach", "frame", "bells", "dream", "magic", "occur"
]
#Set Up Game Variables. We will need variables to:
#store the number of guesses the player has made
#store the different colors we want to use
#keep track of letters that were guessed in the correct position
#letters guessed that were in the incorrect position 
#letters guessed that were not in the word at all.

GREEN = "\033[1;42m"   # Green background
YELLOW = "\033[1;43m"  # Yellow background
GRAY = "\033[1;47m"    # Gray background
RESET = "\033[0m"      # Reset color

# the secret word
secret_word = random.choice(words)

#Create your Welcome message that explains how the game works
print("Welcome to Wordle!")
print("Guess the 5-letter word. You have 6 tries.\n")

#Compare Words Function. Compares the word guessed by the player to the solution word generated at random earlier. Needs to check if each letter of the guess is in the solution word, and if so, if it is in the correct position or not. Then it will print out the guess word again, with each letter colored to reflect whether it was wrong, correct letter but wrong position, or completely correct.
#Game Loop
guesses = 0
while guesses < 6:
    guess = input("Enter a 5-letter word: ").lower()
    if len(guess) != 5 or not guess.isalpha():
        print("Please enter exactly 5 letters.")
        continue
    guesses += 1
    output = ""
    secret_word_used = [False]*5
    #green
    for i in range(5):
        if guess[i] == secret_word[i]:
            output += GREEN + guess[i].upper() + RESET
            secret_word_used[i] = True
        else:
            output += "_" 
    # yellow + gray
    for i in range(5):
        if output[i] != "_":
            continue  # alr green
        letter = guess[i]
        found_yellow = False
        for j in range(5):
            if not secret_word_used[j] and secret_word[j] == letter:
                found_yellow = True
                secret_word_used[j] = True
                break
        if found_yellow:
            output = output[:i] + YELLOW + letter.upper() + RESET + output[i+1:]
        else:
            output = output[:i] + GRAY + letter.upper() + RESET + output[i+1:]
    print(output)
    if guess == secret_word:
        print("You won!")
        break
if guess != secret_word:
    print("Sorry, the word was:", secret_word)