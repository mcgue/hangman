# Hangman game based on
# https://itsourcecode.com/free-projects/python-projects/hangman-game-in-python-with-source-code/

# Import modules
import random
import time

# Start of game
print('Let\'s play Hangman')

# Main module
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""


