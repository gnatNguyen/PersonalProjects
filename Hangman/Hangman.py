import random
import sys
from os import system
import time
import os
import ctypes


# sets title screen of program window
ctypes.windll.kernel32.SetConsoleTitleW("Hangman")
# sets size of program window
os.system('mode con: cols=40 lines=20')
# sets words in word file to a variable, keeping commas as format
words_to_choose = open("words.txt").read()

# turns string of words into a list, splitting by comma
split_words = words_to_choose.split(",")

# randomly chooses a word from the list
word = random.choice(split_words)

# THE TITLE SCREEN, AND ALL OF THE STAGES OF HANGMAN
def welcome_screen():
    print(r"""
                __                
    |_|  /\  |\ | /__ |\/|  /\  |\ | 
    | | /--\ | \| \_| |  | /--\ | \|
            Created by Nhat
               
""")
    print()
    print('    *The whole word can be guessed.*')
    print()
    print("           HIT ENTER TO PLAY")
    print()
    input()
def stage1():
    print(r"""
    |-------
    |      |
    |      |
    |
    |
    |
    |
    |
    |
    |_
    """)
def stage2():
    print(r"""
    |-------
    |      |
    |      |
    |      O
    |     
    |      
    |     
    |
    |
    |_
    """)
def stage3():
    print(r"""
    |-------
    |      |
    |      |
    |      O
    |      |
    |      
    |     
    |
    |
    |_
    """)
def stage4():
    print(r"""
    |-------
    |      |
    |      |
    |      O
    |     /|
    |      
    |     
    |
    |
    |_
    """)
def stage5():
    print(r"""
    |-------
    |      |
    |      |
    |      O
    |     /|\
    |    
    |     
    |
    |
    |_
    """)
def stage6():
    print(r"""
    |-------
    |      |
    |      |
    |      O
    |     /|\
    |      |
    |     
    |
    |
    |_
    """)
def stage7():
    print(r"""
    |-------
    |      |
    |      |
    |      O
    |     /|\
    |      |
    |     / 
    |
    |
    |_
    """)
def death():
    print(r"""
    |-------
    |      |
    |      |
    |      x
    |     /|\
    |      |
    |     / \
    |
    |  You're dead
    |_
    """)
    time.sleep(.5)
    print('The word is ' + '"' + win_word + '"' + '.')
    time.sleep(3)
    sys.exit()
def win_scr():
    print(r"""
__   _____  _   _  __      _____ _  _ 
\ \ / / _ \| | | | \ \    / /_ _| \| |
\ V / (_) | |_| |  \ \/\/ / | || .` |
|_| \___/ \___/    \_/\_/ |___|_|\_|
        """)
def win_scr2():
    print(r"""
 __   _____  _   _  __      _____ _  _ 
 \ \ / / _ \| | | | \ \    / /_ _| \| |
  \ V / (_) | |_| |  \ \/\/ / | || .` |
   |_| \___/ \___/    \_/\_/ |___|_|\_|
        """)
def win_scr3():
    print(r"""
  __   _____  _   _  __      _____ _  _ 
  \ \ / / _ \| | | | \ \    / /_ _| \| |
   \ V / (_) | |_| |  \ \/\/ / | || .` |
    |_| \___/ \___/    \_/\_/ |___|_|\_|
        """)
# simulates win animation screen
def win_animation():
    for x in range(10):
        win_scr()
        time.sleep(.05)
        system('cls')
        win_scr2()
        time.sleep(.05)
        system('cls')
        win_scr3()
        time.sleep(.05)
        system('cls')
    win_scr2()
    time.sleep(.3)
    print('       The word is ' + '"' + win_word + '"' + '!')
    time.sleep(.3)
    print()
    print("       Thank you for playing")
    time.sleep(.3)
    print()
    print("       Have a nice day :)")
    time.sleep(4)
    sys.exit()
    
# Main part which controls player guess inputs
def guess_letter():
    letter = input("Guess a letter: ")
    system('cls')

    # this is win because they guessed it
    if letter == full_norm_word:
        win_animation()

    # sets used_letters list as global
    global used_letters
    if letter in used_letters:

    	# if letter already used, list doesn't change
        used_letters = used_letters
    else:
    	# if not used, letter gets added
        used_letters = used_letters + " " + letter

    # checks is letter is in the word
    if letter in word:

    	# counts how many of the letter there is and outputs that to "amount" variable
        amount = spaced_letter.count(letter)
        if amount > 1:
            print('There are ' + str(amount) + ' "' + letter + '\'s"' + '!')
            # loops through the word
            for x in spaced_letter:
                if x == letter:
                    position = spaced_letter.index(letter)
                    spaces[position] = letter
                    spaced_letter[position] = "_"
        elif amount == 1:
            print('This word contains one ' + '"' + letter + '"' + ".")
            position = spaced_letter.index(letter)
            spaces[position] = letter
        if "_" not in spaces:
            win_animation()            
    else:
        print("This letter is not in here")
        global stage
        stage += 1
        

# plays welcome screen
welcome_screen()
# clears screen
system('cls')
# sets stage to 1, this will be added after every missed word
stage = 1
# makes spaces list, simulates how many letters there are
spaces = []
# loops through word, if a character is a space then creates a space
# if a character then puts an underscore character in the list
for x in word:
    if x == " ":
        spaces = spaces
    else:
        spaces.append("_")

# makes word string into a list comprised of each letter
full_word = list(word)
# gets rid of first character bc it is a "newline" character
full_word.pop(0)
# makes normal word into string
full_norm_word = ''.join(full_word)
spaced_letter = list(word)
# gets rid of first character because "newline" same as normal word
spaces.pop(0)
spaced_letter.pop(0)
# makes space list into string and prints it(shows player how many letters)
space_result = ''.join(spaces)
print(space_result)
space_result = ''.join(spaces)
# makes used letters string
used_letters = ""
# takes the word and makes it into string, therefore if guess is the word then wins
win_word = ''.join(spaced_letter)
win = False
# MAIN LOOOP
while win == False:
    if stage == 1:
        stage1()
    elif stage == 2:
        stage2()
    elif stage == 3:
        stage3()
    elif stage == 4:
        stage4()
    elif stage == 5:
        stage5()
    elif stage == 6:
        stage6()
    elif stage == 7:
        stage7()
    elif stage == 8:
        death()
    guess_letter()
    space_result = ''.join(spaces)
    print(space_result)
    print("You have used " + used_letters)