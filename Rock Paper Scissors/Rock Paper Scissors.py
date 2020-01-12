from getpass import getpass
import sys
import time
from os import system


def titlescr():
    print(r"""
    
     ___  ___  ___  _ __    ___  ___  ___  ___  ___     ___  ___  _  ___  ___  ___  ___  ___ 
    | . \| . ||  _>| / /   | . \| . || . \| __>| . \   / __>|  _>| |/ __>/ __>| . || . \/ __>
    |   /| | || <__|  \    |  _/|   ||  _/| _> |   /   \__ \| <__| |\__ \\__ \| | ||   /\__ \
    |_\_\`___'`___/|_\_\   |_|  |_|_||_|  |___>|_\_\   <___/`___/|_|<___/<___/`___'|_\_\<___/
                                                                                                                                                                             
                                A Rock Paper Scissors Battle - Gnatt
                                        2 PLAYER GAME
                                        
                                        
    """)

titlescr()

time.sleep(2)

name1 = input("Player 1, enter your name: ")
name2 = input("Player 2, enter your name: ")
print("Welcome " + name1 + " and " + name2 + "!")
time.sleep(1)
input("Press ENTER to start ")

def play_againn():
    play_again = input("Play again(y/n)?: ")
    if play_again == "y":
        system('cls')
        titlescr()
        rock_papers()
    else:
        print("Good bye")
        time.sleep(2)
        sys.exit()

def rock_papers():
    win = False
    i = 0
    e = 0
    while win is False:
        time.sleep(2)
        system('cls')
        titlescr()
        print(name1 + "- " + str(i) + "     " + name2 + "- " + str(e))
        p1 = getpass(name1 + " choose r, p, or s: ")
        p2 = getpass(name2 + " choose r, p, or s: ")

        if p1.lower() == "r" and p2.lower() == "p":
            print(name2 + " wins. ")
            e += 1

        elif p1.lower() == "r" and p2.lower() == "s":
            print(name1 + " wins. ")
            i += 1

        elif p1.lower() == "p" and p2.lower() == "r":
            print(name1 + " wins. ")
            i += 1

        elif p1.lower() == "p" and p2.lower() == "s":
            print(name2 + " wins. ")
            e += 1

        elif p1.lower() == "s" and p2.lower() == "r":
            print(name2 + " wins. ")
            e += 1

        elif p1.lower() == "s" and p2 == "p":
            print(name1 + " wins. ")
            i += 1

        elif p1.lower() == p2.lower():
            print("Tie! You are both losers :) ")

        else:
            print("One of you typed an invalid operator. Please learn to read or type. ")

        if i == 3:
            win = True
            system('cls')
            titlescr()
            print(name1 + "- " + str(i) + "     " + name2 + "- " + str(e))
            print(name1 + " WINS")
            play_againn()

        if e == 3:
            win = True
            system('cls')
            titlescr()
            print(name1 + "- " + str(i) + "     " + name2 + "- " + str(e))
            print(name2 + " WINS")
            play_againn()

rock_papers()
