from getpass import getpass
import sys

p1 = getpass("Choose rock, paper, or scissors: ")
p2 = getpass("Choose rock, paper, or scissors: ")

if p1 == "rock" and p2 == "paper":
    print("Player 2 wins ")

elif p1 == "rock" and p2 == "scissors":
    print("Player 1 wins ")

elif p1 == "paper" and p2 == "rock":
    print("Player 1 wins ")

elif p1 == "paper" and p2 == "scissors":
    print("Player 2 wins ")

elif p1 == "scissors" and p2 == "rock":
    print("Player 2 wins ")

elif p1 == "scissors" and p2 == "paper":
    print("Player 1 wins ")

elif p1 == "rock" and p2 == "rock":
    print("Tie :( ")

elif p1 == "paper" and p2 == "paper":
    print("Tie :( ")

elif p1 == "scissors" and p2 == "scissors":
    print("Tie :( ")

else:
    print("One of you typed an invalid operator. Please learn to read or type. ")

input("Press enter to exit. ")
sys.exit()