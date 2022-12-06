"""
Written By Brendan Richards, Instructor Brad Lythgoe. 
I do not believe it was necessary for me to use 4+ classes. I think lists within lists are very
useful. Sometimes I feel like I can accomplish things easier with lists than classes. If this isnt
OK, please email me.
"""

import math
import random
import numpy as np
from colorama import Fore, Style

# set gameplay conditions
score = 0
playing = "true"

# choose word and matching letters with word
class wordpicker:
    words = [['earth', ['e','a','r','t','h']], ['slice',['s','l','i','c','e']], ['crazy',['c','r','a','z','y']], ['jerky',['j','e','r','k','y']]]
    randomizer = random.randint(0, 3)
    chosen_word = words[randomizer][0]
    letter_list = words[randomizer][1]

# print the word, debugging use only
# print(wordpicker.chosen_word, "THIS")

# set guesses to empty
class hangmanlist:
    correct_guesses = wordpicker.letter_list
    char_guesses = ['_', '_', '_', '_', '_']

class winner:
    head = "  \\0/"
    torso = "    |"
    legs = "   / \\"
    box = "[][][][][]"

# printing for the jumper + parachute depending on game score
def print_jumper(score):
    parachute = ['  ___', ' /___\\', ' \\   /', '  \\ /']
    human = ['   0', '  /|\\', '  / \\', '', '^^^^^^^']
    # always print human, print decaying amounts of parachute
    for i in range(score, 4):
        print(parachute[i])

    # print dead body
    for element in human:
        if score == 4:
            #dead body
            print(f"  \\x/ \n   |\n{human[2]}\n{human[4]}")
            print(f"YOU LOSE")
            print(f"Your word was {wordpicker.chosen_word}!")
            break
        print(element)

# get player guesses
def player_guesses():
    guess = str(input("Guess a letter [a-z]: "))
    return guess

while playing == "true":

    print_jumper(score)
    print(*hangmanlist.char_guesses)
    guess = player_guesses()


    # is player guess correct?
    if guess in wordpicker.letter_list: # is the guess in the char list?
        np_array = np.array(wordpicker.letter_list)
        for element in wordpicker.letter_list: # where does it match?
            if guess == element:
                index = wordpicker.letter_list.index(element)
                hangmanlist.char_guesses[index] = element # set _ _ _ _ _ = to guess
                print("Match!")
        
        # if the lists match, you win + game over 
    if wordpicker.letter_list == hangmanlist.char_guesses: 
        print("\n",winner.head)
        print(winner.torso)
        print(winner.legs)
        print(Fore.GREEN + winner.box)
        print(Style.RESET_ALL)
        print(f"You Win!")
        break

        # if you guess wrong, and you guess wrong 5 times, you lose. 
    if guess not in wordpicker.letter_list:
        print("No match! \n")
        score = score + 1
        if score == 4:
            print_jumper(score)
            break            

