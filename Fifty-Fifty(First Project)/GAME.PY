import sys
import time
import os
from getpass import getpass
from threading import Thread
from threading import Timer
from os import remove
from os import system
from sys import argv
import vlc

# list of sounds
harmony = vlc.MediaPlayer("sounds/harmony.mp3")
death = vlc.MediaPlayer("sounds/oof.mp3")
bing = vlc.MediaPlayer("sounds/bing.mp3")
creepy = vlc.MediaPlayer("sounds/creepy.mp3")
medieval = vlc.MediaPlayer("sounds/medieval.mp3")
battle = vlc.MediaPlayer("sounds/battle.mp3")
text = vlc.MediaPlayer("sounds/asriel.mp3")
notif = vlc.MediaPlayer("sounds/powerup.mp3")
door = vlc.MediaPlayer("sounds/door.mp3")
key = vlc.MediaPlayer("sounds/key.mp3")
walk = vlc.MediaPlayer("sounds/walk.mp3")
chew = vlc.MediaPlayer("sounds/chew.mp3")
start = vlc.MediaPlayer("sounds/cassette.mp3")
sadsong = vlc.MediaPlayer("sounds/sadsong.mp3")
boom = vlc.MediaPlayer("sounds/explosion.mp3")
ticking = vlc.MediaPlayer("sounds/time.mp3")
shining = vlc.MediaPlayer("sounds/shining.mp3")
winsong = vlc.MediaPlayer("sounds/winning.mp3")


# list of lists
yeslist = ["yes", "y", "Yes", "Yeah", "yeah"]
nolist = ["no", "n", "No"]
colorlist = ["pink", "blue", "black", "white", "Pink", "Blue", "White", "Black"]
redList = ["red", "Red"]
startlist = ["start game", "Start Game", "Start", "start", "Start game", "start Game"]

time.sleep(1)
start.play()
time.sleep(1.5)
print()
print("                         L        O       A       D       I       N       G                                   ")
print()
for x in range(101):
    time.sleep(0.05)
    print("█", sep=' ', end='', flush=True)
print()
time.sleep(1)
print("                                         LOADING COMPLETE!                                                     ")
time.sleep(3)
system('cls')
time.sleep(1)
vlc.MediaPlayer.audio_set_volume(harmony, 100)
harmony.play()
print("      _________                                                                                            ")
time.sleep(0.1)
print("     |         |           ________      __       __       __                 _______         ____         ")
time.sleep(0.1)
print("     |    _____|  .__.    /   __   \    |  |     |  |     |  |               |   ____|       /    \        ")
time.sleep(0.1)
print("     |   |        |__|    |  |  |  |  __|  |__    |  |   |  |                |  |           /  __  \       ")
time.sleep(0.1)
print("     |   |____            |  |  |__| |__    __|    |  |_|  |                 |  |___       |  /  \  |      ")
time.sleep(0.1)
print("     |       |     __     |  |___       |  |        |     |       _____      |___   \      | |    | |      ")
time.sleep(0.1)
print("     |   ____|    |  |    |   ___|      |  |         |   |       |_____|          \  |     | |    | |      ")
time.sleep(0.1)
print("     |   |        |  |    |  |          |  |         |   |                        |  |     |  \__/  |      ")
time.sleep(0.1)
print("     |   |        |  |    |  |          |  |         |   |                   ____ /  |      \      /       ")
time.sleep(0.1)
print("     |___|        |__|    |__|          |__|         |___|                  |_______/        \____/        ")
print()

time.sleep(2)
blink = 0
blinklimit = 3
print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
while blink < blinklimit:
    print("                        W E L C O M E ", end="                                  \r")
    time.sleep(0.8)
    print("                                               D E A R ", end="\r")
    time.sleep(0.8)
    print("                                                             P L A Y E R ", end="\r")
    time.sleep(0.8)
    blink += 1
print("█                                    C R E A T E D     B Y     N H A T                              █")
print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
time.sleep(2)
print()


def spfast(string):
    text.play()
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.06)
    text.stop()
    time.sleep(1)
    print()


def spslow(string):
    text.play()
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.07)
    text.stop()
    time.sleep(1)
    print()


def spSUPERFAST(string):
    text.play()
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.0005)
    text.stop()
    time.sleep(1)
    print()


def winscreen():
    system('cls')
    spSUPERFAST(r""""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@****************************************************************************************************************************@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@%%#............................................................................................................................#%&@@@@@@@@@@@@@@@
@@@@@@@@@@@.................................................................................................................................*@@@@@@@@@@@@@@@
@@@@@@@@@@@.................................................................................................................................*@@@@@@@@@@@@@@@
@@@@@@@@@@@.......%@%...........%@@....%@@@@@@%....@@%......*@@.........%@@.......@@.......@@%..@@@@@@@@@@@%..@@*......%@@..@@%..@@..*@@....*@@@@@@@@@@@@@@@
@@@@@@@@@@@.......%@%...........%@@..@@*......*@@..@@%......*@@.........%@@.......@@.......@@%......*@@.......@@@@@....%@@..@@%..@@..*@@....*@@@@@@@@@@@@@@@
@@@@@@@@@@@.........*@@.......@@*....@@*......*@@..@@%......*@@.........%@@.......@@.......@@%......*@@.......@@*..@@..%@@..@@%..@@..*@@....*@@@@@@@@@@@@@@@
@@@@@@@@@@@..........**%%,.,%%**.....@@*......*@@..@@%......*@@.........%@@.......@@.......@@%......*@@.......@@*..**%%@@@..@@%..@@..*@@....*@@@@@@@@@@@@@@@
@@@@@@@@@@@............@@*.*@@.......@@*......*@@..@@%......*@@.........%@@.......@@.......@@%......*@@.......@@*....@@@@@..@@%..@@..*@@....*@@@@@@@@@@@@@@@
@@@@@@@@@@@..............%@%.........@@*......*@@..@@%......*@@.........%@@.......@@.......@@%......*@@.......@@*......%@@..@@%..@@..*@@....*@@@@@@@@@@@@@@@
@@@@@@@@@@@..............%@%.........@@*......*@@..@@%......*@@.........%@@.......@@.......@@%......*@@.......@@*......%@@..@@%..@@..*@@....*@@@@@@@@@@@@@@@
@@@@@@@@@@@..............%@%.........@@*......*@@..@@%......*@@.........%@@.......@@.......@@%......*@@.......@@*......%@@..@@%..@@..*@@....*@@@@@@@@@@@@@@@
@@@@@@@@@@@..............%@%.........@@*......*@@..@@%......*@@.........%@@.......@@.......@@%......*@@.......@@*......%@@..@@%..@@..*@@....*@@@@@@@@@@@@@@@
@@@@@@@@@@@..............%@%.........@@*......*@@..@@%......*@@.........%@@.......@@.......@@%......*@@.......@@*......%@@..@@%..@@..*@@....*@@@@@@@@@@@@@@@
@@@@@@@@@@@..............%@%.........@@*......*@@..@@%......*@@.........%@@.......@@.......@@%......*@@.......@@*......%@@..@@%..@@..*@@....*@@@@@@@@@@@@@@@
@@@@@@@@@@@..............%@%.........@@*......*@@..@@%......*@@.........%@@.......@@.......@@%......*@@.......@@*......%@@..@@%..@@..*@@....*@@@@@@@@@@@@@@@
@@@@@@@@@@@..............%@%.........@@*......*@@..@@%......*@@.........%@@.......@@.......@@%......*@@.......@@*......%@@..@@%..@@..*@@....*@@@@@@@@@@@@@@@
@@@@@@@@@@@..............%@%.........@@*......*@@..@@%......*@@............@@.....@@.....@@.........*@@.......@@*......%@@..................*@@@@@@@@@@@@@@@
@@@@@@@@@@@..............%@%...........%@@@@@@%......*@@@@@@%................@@@@@..@@@@@....*@@@@@@@@@@@@@%..@@*......%@@..@@%..@@..*@@....*@@@@@@@@@@@@@@@
@@@@@@@@@@@.................................................................................................................................*@@@@@@@@@@@@@@@
@@@@@@@@@@@.................................................................................................................................*@@@@@@@@@@@@@@@
@@@@@@@@@@@..................................................................................................................................@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@............................................................................................................................@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""")
    spfast("Wow look at you all cool and spiffy.")
    spfast("Made it to the end :)")
    spfast("There will be bigger and better projects in the future.")
    spfast("Thank you so much for playing.")
    spfast("Our adventure ends here...")
    spfast("Good bye!")
    time.sleep(2)
    sys.exit()


def die():
    blink = 0
    blinklimit = 3
    while blink < blinklimit:
        print("▀▀▀ ", end="                                     \r")
        time.sleep(0.05)
        print("     ▀▀▀", end="\r")
        time.sleep(0.05)
        print("         ▀▀▀ ", end="\r")
        time.sleep(0.05)
        print("             ▀▀▀ ", end="\r")
        time.sleep(0.05)
        print("                 ▀▀▀ ", end="\r")
        time.sleep(0.05)
        print("                     ▀▀▀ ", end="\r")
        time.sleep(0.05)
        print("                         ▀▀▀ ", end="\r")
        time.sleep(0.05)
        print("                     ▀▀▀ ", end="\r")
        time.sleep(0.05)
        print("                 ▀▀▀ ", end="\r")
        time.sleep(0.05)
        print("             ▀▀▀ ", end="\r")
        time.sleep(0.05)
        print("         ▀▀▀ ", end="\r")
        time.sleep(0.05)
        print("     ▀▀▀ ", end="\r")
        time.sleep(0.05)
        print("▀▀▀ ", end="\r")
        time.sleep(0.05)
        blink += 1


def titlescr():
    system('cls')
    print("      _________                                                                                            ")
    print("     |         |           ________      __       __       __                 _______         ____         ")
    print("     |    _____|  .__.    /   __   \    |  |     |  |     |  |               |   ____|       /    \        ")
    print("     |   |        |__|    |  |  |  |  __|  |__    |  |   |  |                |  |           /  __  \       ")
    print("     |   |____            |  |  |__| |__    __|    |  |_|  |                 |  |___       |  /  \  |      ")
    print("     |       |     __     |  |___       |  |        |     |       _____      |___   \      | |    | |      ")
    print("     |   ____|    |  |    |   ___|      |  |         |   |       |_____|          \  |     | |    | |      ")
    print("     |   |        |  |    |  |          |  |         |   |                        |  |     |  \__/  |      ")
    print("     |   |        |  |    |  |          |  |         |   |                   ____ /  |      \      /       ")
    print("     |___|        |__|    |__|          |__|         |___|                  |_______/        \____/        ")
    print()
    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    print("█                                    C R E A T E D     B Y     N H A T                              █")
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print()


spfast("CHOOSE YOUR DIFFICULTY")
text.play()
string = '| Ez pz (1)  | Kinda Easy (2) | Rock Hard (3) | \n'
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)
text.stop()
time.sleep(.5)
level = input("Which one(1, 2, or 3)?: ")
if level == "1":
    spslow("You have 3 lives.")
    time.sleep(2)

elif level == "2":
    spslow("You have 2 lives.")
    time.sleep(2)

elif level == "3":
    spslow("You have 1 life.")
    time.sleep(2)

titlescr()

text.play()
string = 'What is your name? \n'
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.08)
text.stop()
time.sleep(.2)
name = input("--> : ")
text.play()
string = 'Create a password (INPUT IS HIDDEN) \n'
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.07)
text.stop()
time.sleep(.2)
password = getpass("--> : ")

# name and pass input
print()
string = '              Q U I C K    N O T E S \n'
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)
time.sleep(.5)
print("╻___________________________________________________╻")
time.sleep(.3)
print("║           This is a choice based game.            ║")
time.sleep(.3)
print("║            No CAPS needed for responses           ║")
time.sleep(.3)
print("║  DO NOT PUT A SPACE IN FRONT OR END OF ANSWERS    ")
time.sleep(.3)
print("║  NOTE: CMD pauses if you click,                   ║")
time.sleep(.3)
print("║        just press some other key to resume        ║")
time.sleep(.3)
print("║ >>>> DO NOT PRESS ANYTHING UNLESS PROMPTED <<<<   ║")
time.sleep(.3)
print("║___________________________________________________║")

time.sleep(3)
print()
startgame = startlist

# start game commands
while startgame not in startlist:
    startgame = input("Type \"play\" to start: ")
    # start game
    if startgame == "play":
        harmony.stop()
        bing.play()
        time.sleep(3)
        print("Hello " + name + "! Nice to meet you. ")
        time.sleep(2)
        color = input("I really like the color red, what's yours?: ")
        bing.stop()
        time.sleep(1)
        if color in redList:
            spslow("I'm liking you already :)")
            spslow("Here, take this...")
            time.sleep(1)
            notif.play()
            print("YOU RECEIVED AN EXTRA TRY!")
            time.sleep(2)
            spslow("Let's begin.")
            notif.stop()
            break
        elif color in colorlist:
            spslow("I like that color too!")
            spslow("Let's begin.")
            break
        else:
            spfast("You were probably never loved...")
            spslow("Let's begin.")
                # introduction with color
            break
    # inputs invalid commands
    else:
        spslow("Invalid statement.")
        continue


# main function game
def main():
    vlc.MediaPlayer.audio_set_volume(harmony, 100)

    i = 0
    tries = 0
    if level == "1":
        tries += 3

    elif level == "2":
        tries += 2
    elif level == "3":
        tries += 1

    if color in redList:
        tries += 1

    while i < tries:

        yeslist = ["yes", "y", "Yes", "Yeah", "yeah"]
        nolist = ["no", "n", "No"]
        colorlist = ["pink", "blue", "black", "white", "Pink", "Blue", "White", "Red", "Black", "red"]
        startlist = ["start game", "Start Game", "Start", "start", "Start game", "start Game", "s", "S", "game", "Game"]

        medieval.play()
        time.sleep(2)
        q1 = input("Can you spell red?: ")
        if q1 in yeslist:
            spfast("Okay, so you aren't that stupid.")
            spfast("Onwards we go!")

            # player chooses door
            spfast("You turn into a dimly lit corridor and see two doors.")
            print(r"""
            
               ,-' ;  ! `-.             ,-' ;  ! `-.
              / :  !  :  . \           / :  !  :  . \
             |_ ;   __:  ;  |         |_ ;   __:  ;  |  
             )| .  :)(.  !  |         )| .  :)(.  !  | 
             |"    (##)  _  |         |"    (##)  _  |  
             |  :  ;`'  (_) (         |  :  ;`'  (_) (  
             |  :  :  .     |         |  :  :  .     |  
             )_ !  ,  ;  ;  |         )_ !  ,  ;  ;  |  
             || .  .  :  :  |         || .  .  :  :  |  
             |" .  |  :  .  |         |" .  |  :  .  |  
             |_____;----.___|         |_____;----.___|  
                    RED                      BLUE            
                           
                                                        """)
            time.sleep(1)
            print()
            door_question = input("Which door do you enter?: ")
            if door_question in redList:
                door.play()
                time.sleep(1)
                spfast("A musty scent hits you as the door opens.")
                spfast("The door closes behind, urging you foward.")
                spfast("Ahh, you must be " + name + " - says a voice. ")
                time.sleep(3)
                door.stop()
                old_manquestion = input("Ask him who he is: ")
                time.sleep(1)
                spfast(old_manquestion + " you ask? I am Dinh Linh. ")
                time.sleep(3)
                spfast("If you look behind me, you'll notice a chest.")
                spfast("It requires a password to enter.")

                # enter password
                attempt = 0
                for attempt in range(3):
                    chest_input = input("What is the password?: ")
                    if chest_input == password:
                        break
                    else:
                        attempt += 1
                        if attempt == 2:
                            spfast("Hmmm, it looks like you don't know the passowrd.")
                            spfast("Guess I gotta call it a warp.")
                            spslow("Everything goes black.")
                            for x in range(3):
                                time.sleep(1)
                                print(".", end="", flush=True)
                                time.sleep(1)
                            print()
                            spslow("You have died...")
                            spfast("ACTUALLY... I'll give you one more try. ")
                            spfast("BUT... You will completely lose if incorrect.")
                            retry_password = input("What is your password?: ")
                            time.sleep(1)
                            if retry_password == password:
                                spfast("FINALLY! Glad you aren't incompetent.")
                                break

                            else:
                                spfast("Sorry that is incorrect...")
                                spfast("Looks like I gotta call it a wrap.")
                                spslow("Good bye!")
                                for x in range(50):
                                    time.sleep(0.05)
                                    print("█", sep=' ', end='', flush=True)
                                    time.sleep(1)
                                print()
                                spslow("File has been deleted.")
                                sys.exit()

                        else:
                            spfast("Oops, that isn't the correct password.")
                            spfast("I'll give you one more try.")
                            continue

                key.play()
                time.sleep(3)
                print(r"""
                
                                 _.--.
                            _.-'_:-'||
                        _.-'_.-::::'||
                   _.-:'_.-::::::'  ||
                 .'`-.-:::::::'     ||
                /.'`;|:::::::'      ||_
               ||   ||::::::'     _.;._'-._
               ||   ||:::::'  _.-!oo @.!-._'-.
               \'.  ||:::::.-!()oo @!()@.-'_.|
                '.'-;|:.-'.&$@.& ()$%-'o.'\U||
                  `>'-.!@%()@'@_%-'_.-o _.|'||
                   ||-._'-.@.-'_.-' _.-o  |'||
                   ||=[ '-._.-\U/.-'    o |'||
                   || '-.]=|| |'|      o  |'||
                   ||      || |'|        _| ';
                   ||      || |'|    _.-'_.-'
                   |'-._   || |'|_.-'_.-'
                    '-._'-.|| |' `_.-'
                        '-.||_/.-'

                """)
                time.sleep(1)
                spfast("There are two items inside.")
                key.stop()

                #player chooses item
                chestlistA=["a", "A"]
                chestlistB=["b", "B"]
                item_chest = input("Do you want item A or B?: ")
                # chooses chicken nugget
                if item_chest in chestlistA:
                    spfast("Linh hands you a small object.")
                    for x in range(3):
                        time.sleep(1)
                        print(".", end="", flush=True)
                        time.sleep(1)
                    print()
                    notif.play()
                    print("You obtained a CHICKEN NUGGET! ")
                    time.sleep(2)
                    notif.stop()

                    # chooses sword
                elif item_chest in chestlistB:
                    spfast("Linh hands you a heavy object.")
                    for x in range(3):
                        time.sleep(1)
                        print(".", end="", flush=True)
                    print()
                    notif.play()
                    print("You obtained a GREAT SWORD! ")
                time.sleep(2)
                spfast("On you go " + name + ". I would wish you luck, but you're probably gonna fail. ")
                time.sleep(3)
                notif.stop()

                # throw away nugget?
                if item_chest in chestlistA:
                    spfast("You look at the moldy nugget in disgust.")
                    throwaway_chicken = input("Throw it away?: ")
                    if throwaway_chicken in yeslist:
                        time.sleep(1)
                        spfast("You toss the nugget into a pile of bones.")
                        spfast("Probably didn't need it anyways.")
                    elif throwaway_chicken in nolist:
                        spfast("You decide to keep the nugget.")
                        spfast("Might come in handy.")

                        # throw sword away?
                elif item_chest in chestlistB:
                    throwswordlist=["Throw it", "throw it", "toss it", "Toss it"]
                    keepswordlist = ["keep it", "Keep it", "keep", "Keep"]
                    spfast("You examine the sword a little closer.")
                    spfast("It is beautifully crafted, but quite heavy.")
                    spfast("Could potentially slow you down.")
                    throwaway_sword = input("Toss the sword or keep it?: ")
                    time.sleep(2)
                    if throwaway_sword in throwswordlist:
                        spfast("The sword makes a loud clang as it hits the ground.")
                        spfast("Oh well, you're a weakling so it was for the best.")
                    elif throwaway_sword in keepswordlist:
                        spfast("Although it is heavy, you decide to keep it.")

                medieval.stop()
                time.sleep(1)
                creepy.play()
                walk.play()
                spfast("Guided by the flickering torches, you continue into the unknown.")
                spfast("An hour passes.")
                spfast("The endless reach of the hallway looms as your will push you forward.")
                spfast("As you're reaching exhaustion, you stumble upon dividing pathways.")
                walk.stop()
                spfast("The right path is completely dark and reeks of blood.")
                spfast("However, there is a box of somewhat intact flashlights.")
                spfast("The left path has lit torches guiding the way.")
                spfast("But the sense of an eerie darkness stil exists")
                time.sleep(3)
                listright=["right", "Right"]
                listleft = ["left", "Left"]
                path_way = input("Enter the right or left?: ")
                time.sleep(1)

                # ENTER THE RIGHT PATHWAY
                if path_way in listright:
                    spfast("You pick up a flashlight and turn it on.")
                    spfast("Finding that it works, you enter into the darkness.")
                    spfast("Strangely, it's reeeeaaalllllyyyyy quiet...")
                    creepy.stop()
                    battle.play()
                    spfast("SOMETHING APPEARS FROM THE LOOMING DARKNESS!!!")

                       # if player chose ITEM A - NUGGET
                    if item_chest in chestlistA:
                        spfast("You reach for the chicken nugget...")

                        # if player tossed away nugget ---- END
                        if throwaway_chicken in yeslist:
                            spfast("OH NO! YOU THREW IT AWAY.")
                            spfast("With nothing to defend yourself, you are painfully eaten.")
                            spfast("Natural selection I guess.")
                            battle.stop()
                            die()
                            death.play()
                            print()
                                # message box for restart
                            spfast("You have died...")
                            time.sleep(1)
                            titlescr()
                            i += 1
                            print("***************** GAME RESTARTED *****************")
                            print("█ " + str(i) + "/3 attempts █")
                            death.stop()
                            medieval.play()
                            continue

                        # if player kept nugget-- CONTNUE
                        elif throwaway_chicken in nolist:
                            eatlist=["eat it", "Eat it", "eat", "Eat"]
                            throwlist=["Throw it", "throw it", "throw", "Throw"]
                            attack_nugget = input("Do you eat it, or throw it at the creature?: ")
                            time.sleep(1)
                            if attack_nugget in eatlist:
                                time.sleep(1)
                                chew.play()
                                spfast("An OVERWHELMING force surges through your body.")
                                spfast("You charge at it like a WEAB!")
                                chew.stop()
                                spfast("SKRRT    SKRRRRTT       SSKKKKRRTTTTTT")
                                spfast("You absolutely demolish the poor creature in one punch.")
                                spfast("The power of nuggies and weabs run through your veins.")


                                # if player throws the nugget at creature -- END
                            elif attack_nugget in throwlist:
                                spfast("You toss the nugget with the arm of a little girl.")
                                spfast("It doesn't seem to be affected...")
                                spfast("Seeming to be annoyed, it jumps and crushes you.")
                                spfast("What kind of idiot would throw a nugget...?")
                                battle.stop()
                                time.sleep(1)
                                die()
                                death.play()
                                print()
                                    # message box for restart
                                spslow("You have died...")
                                time.sleep(1)
                                titlescr()
                                i += 1
                                print("***************** GAME RESTARTED *****************")
                                print("█ " + str(i) + "/3 attempts █")
                                death.stop()
                                medieval.play()
                                continue

                        # if player chooses ITEM B - SWORD
                    elif item_chest in chestlistB:
                        spfast("You quickly reach for the sword!")

                            # if sword was thrown away
                        if throwaway_sword in throwswordlist:
                            spfast("YIKES, you threw it away remember?")
                            spfast("You desperately try to ru-")
                            spfast("Helplessly pinned down, the creature makes a quick meal.")
                            battle.stop()
                            time.sleep(1)
                            spfast("Everything goes black.")
                            die()
                            death.play()
                            print()
                                # message box for restart
                            spfast("You have died...")
                            time.sleep(1)
                            titlescr()
                            i += 1
                            print("***************** GAME RESTARTED *****************")
                            print("█ " + str(i) + "/3 attempts █")
                            death.stop()
                            medieval.play()
                            continue


                                # time inputs for fighting sequence
                        elif throwaway_sword in keepswordlist:
                            # blocking thing
                            timeout = 3
                            t = Timer(timeout, print, ['You didn\'t block in time...' ' Hit Enter'])
                            t.start()
                            prompt = "You have %d seconds to counter, TYPE IN A!\n" % timeout
                            attack_A = input(prompt)
                            t.cancel()

                            a_List = ["a", "A"]

                            # if b is pressed
                            if attack_A in a_List:
                                time.sleep(2)
                                spfast("You countered its attack with a powerful swing!")
                                spfast("By the power of dark people, you valiantly TRUMP the creature.")
                                spfast("You feel stronger than before.")
                                hurt = False

                            # misses b move - hurt really badly
                            elif attack_A not in a_List:
                                time.sleep(2)
                                spfast("You failed to counter...")
                                spfast("It slashes your legs, but decides to spare you.")
                                spfast("Your legs are wounded.")
                                hurt = True


                        # continue to story if survive creature encounter
                        battle.stop()
                        time.sleep(1)
                        shining.play()
                        time.sleep(1)
                        spfast("You find that the creature was protecting some kind of door.")
                        spslow("You notice that it is locked with a keypad.")
                        spslow("You find two chests, and a note that reads:")
                        spslow("One of these chests contain a useful clue.")
                        spslow("The box you don't open will disappear")
                        spfast("Choose wisely.")
                        rightList = ["right", "Right"]
                        leftList = ["left", "Left"]
                        keypadbox = input("Will you open the right or the left one?: ")
                        time.sleep(.5)
                        if keypadbox in rightList:
                            notif.play()
                            print("YOU FOUND A NOTE")
                            time.sleep(2)
                            spslow("It says...")
                            spfast("100% of people who drink water... die.")
                            spfast("Also, to open this door you need a number.")
                            spfast("The other box had the actual guide.")
                        elif keypadbox in leftList:
                            notif.play()
                            print("YOU FOUND A NOTE")
                            time.sleep(2)
                            spslow("It says...")
                            spslow("The code is a number between 1 and 6")
                            spslow("You have 3 tries.")
                            spfast("If you run out of tries, the door wil detonate.")

                            # guessing game for door
                        spfast("You flip open the keypad revealing 9 digits.")
                        keypadtries = 0
                        keypadlimit = 3
                        keypadnum = "4"
                        while keypadtries < keypadlimit:
                            keypad = input("Choose a number: ")
                            if keypad == keypadnum:
                                time.sleep(1)
                                spfast("You guessed the code right!")
                                break
                            elif keypad < keypadnum:
                                keypadtries += 1
                                numb = (keypadlimit - keypadtries)
                                spfast("Your guess was too low!")
                                spfast("You have " + str(numb) + " tries left. ")
                                time.sleep(2)
                                continue
                            elif keypad > keypadnum:
                                keypadtries += 1
                                numb = (keypadlimit - keypadtries)
                                spfast("Your guess was too high!")
                                spfast("You have " + str(numb) + " tries left. ")
                                time.sleep(2)
                                continue
                        else:
                            shining.stop()
                            ticking.play()
                            spfast("Loud ticks come from behind the door...")
                            spfast("I THINK YOU SHOU-")
                            ticking.stop()
                            boom.play()
                            time.sleep(1)
                            spfast("Everything goes black.")
                            boom.stop()
                            print()
                            die()
                            death.play()
                            print()
                            # message box for restart
                            spfast("You have died...")
                            time.sleep(1)
                            titlescr()
                            i += 1
                            print("***************** GAME RESTARTED *****************")
                            print("█ " + str(i) + "/3 attempts █")
                            death.stop()
                            medieval.play()
                            continue

                        spfast("A path seemingly appears out of nowhere.")
                        spfast("There are shiny gold coins littering the ground. ")
                        spfast("Looks as if a trail leading somewhere.")
                        spfast("Do you want to pick them up?")
                        goldget = input("(yes/no): ")
                        if goldget == "yes":
                            gold = True
                        elif goldget == "no":
                            gold = False
                        spfast("You follow the endless trail of coins.")
                        spfast("Wonder who put these coins here...")
                        spfast("You start wondering other things.")
                        spfast("Time seems to have stopped since you started this journey.")
                        spfast("Time is something you could never get back.")
                        spfast("It felt as if you've wasted your life following others")
                        spfast("...")
                        spfast("The hell was that?")
                        spfast("\"Ahhhhhh, " + name + " you actually made it to the end!\"")
                        spfast("As you approach the figure, you notice he looks familiar.")
                        spfast("\"Before I let you pass, answer one last question.\"")
                        spfast("\"What is my name?\"")
                        nameee = ["linh dinh", "Linh Dinh", "linh Dinh", "Linh dinh"]
                        winname = input("(full name): ")
                        if winname in nameee:
                            spfast("CORRRECCCTTT")
                            spfast("\"Im so happy you remember me!\"")
                            spfast("\"For that I think I'll let you go.\"")
                            spfast("\"Actually, hold on, did you happen to see a gold trail?\"")
                            time.sleep(1)
                            spfast("\"YOU DID?\"")
                            spfast("\"Did you pick it up?\"")
                            goldgain = input("(yes/no): ")
                            if goldgain in yeslist:
                                if gold == True:
                                    spfast("\"THANK YOU! I've been looking everywhere for that.\"")
                                    spfast("\"Alright " + name + ", it's been fun.\"")
                                    spfast("You may leave...")
                                    time.sleep(2)
                                    shining.stop()
                                    winscreen()
                                elif gold == False:
                                    spfast("\"You don't have it...")
                                    spfast("\"Why would you lie to me...\"")
                                    spfast("\"YOU SHALL FACE MY WRATH!!!\"")
                                    spfast("\"REEEEEEEEEEEEEEEEEEEEEEEEEEE\"")
                                    shining.stop()
                                    spfast("You died...")
                                    death.play()
                                    time.sleep(1)
                                    titlescr()
                                    i += 1
                                    print("***************** GAME RESTARTED *****************")
                                    print("█ " + str(i) + "/3 attempts █")
                                    death.stop()
                                    medieval.play()
                                    continue
                            elif goldgain in nolist:
                                spfast("\"I'm glad you didn't lie to me.\"")
                                spfast("\"But I'm very sorry, that was precious to me.\"")
                                spfast("\"You won't be leaving my dungeon\"")
                                shining.stop()
                                spfast("You died...")
                                death.play()
                                time.sleep(1)
                                titlescr()
                                i += 1
                                print("***************** GAME RESTARTED *****************")
                                print("█ " + str(i) + "/3 attempts █")
                                death.stop()
                                medieval.play()
                                continue
                        else:
                            spfast("I'm so sad you don't remember me...")
                            spfast("I thought we were friends " + name + ". ")
                            spfast("REEEEEEEEEEEEEEEEEEEEE")
                            spfast("You died...")
                            time.sleep(1)
                            titlescr()
                            i += 1
                            print("***************** GAME RESTARTED *****************")
                            print("█ " + str(i) + "/3 attempts █")
                            death.stop()
                            medieval.play()
                            continue

                # ENTER THE LEFT PATHWAY
                if path_way in listleft:
                    spfast("You enter the left pathway.")
                    spfast("It turns out to be a circular room.")
                    spfast("In the middle of the room is a small table with three cups.")
                    time.sleep(1)
                    print(r"""
                      ```         ```         ```
                    /.---.\     /.---.\     /.---.\             
                    |`````|     |`````|     |`````|
                    \  P  /     \  B  /     \  G  /
                     `-.-'       `-.-'       `-.-' 
                       |           |           | 
                     __|__       __|__       __|__  
                     
                    """)
                    spfast("Each cup has a different color ---- pink, black, and green.")
                    spfast("\"Type the color to see it's properties.\"")
                    spfast("Type \"drink (color)\" to drink the contents of a cup.")
                    drank = False
                    dead = False
                    drunk = False
                    win = False
                    while drank == False:
                        drink = input("What do you do?: ")
                        if drink == "pink":
                            spfast("This has the simplest of designs compared to the other chalices, yet it looked the most refined.")
                            spfast("The liquid contained in it is odorless, and has a warm, blush color.")
                            spfast("It is translucent, a bit more on the opaque side, so you can’t tell exactly what the consistency would be like.")
                        elif drink == "black":
                            spfast("This chalice has a matte finish and more intricate – different from the other two.")
                            spfast("There are engravings in what looks like a language you aren't familiar with.")
                            spfast("The liquid in it is stark black against the white of the cup, with swirls of sparkles inside of it, reminding you of space.")
                            spfast("It has a scent you can’t describe, but, somehow, it lures you in.")
                        elif drink == "green":
                            spfast("This cup is silver with glass accents, letting you see the liquid through the cup.")
                            spfast("The liquid inside is a pale green, soft and unassuming, despite the unusual color.")
                            spfast("It is more milky looking, reminding you of a drink you were fond of in your childhood.")
                        elif drink == "drink pink":
                            dead = True
                            break
                        elif drink == "drink black":
                            win = True
                            break
                        elif drink == "drink green":
                            drunk = True
                            break
                        else:
                            spfast("That is an invalid action...")


                if dead == True:
                    spfast("You drink the pink liquid.")
                    spfast("It's thick and sweet but burns as it goes down.")
                    spfast("It feels as though it's melting your insides.")
                    spfast("You drop the cup...")
                    spfast("You notice there is text on the bottom.")
                    spfast("\"Bleach\"")
                    spfast("Everything goes black.")
                    print()
                    die()
                    death.play()
                    print()
                    # message box for restart
                    spfast("You have died...")
                    time.sleep(1)
                    titlescr()
                    i += 1
                    print("***************** GAME RESTARTED *****************")
                    print("█ " + str(i) + "/3 attempts █")
                    death.stop()
                    medieval.play()
                    continue

                if drunk == True:
                    spfast("You take a careful sip.")
                    spfast("It unexpectedly has a wonderful taste.")
                    spfast("You down the substance quickly, immediately wanting more.")
                    spfast("The bottom of the cup is labeled, \"99% slow acting alcohol\".")
                    spfast("Whatever that means.")
                    time.sleep(1.5)
                    spfast("A path seemingly appears out of nwhere.")
                    spfast("Thre are shny gold coins literd on the ground ")
                    spfast("Lo%ks as if a trail leadng %%s%ome%w%he%%re.")
                    spfast("D..o yu w$$%n^%t t#o pck th^m up$$?")
                    goldget = input("(yes/no): ")
                    if goldget == "yes":
                        gold = True
                    elif goldget == "no":
                        gold = False
                    spfast("yu st$rt folow*ng t@h%e tr%%ail% of g%%od.")
                    spfast("s%$%ight sta%$rts $%#$to fli%^%%$ckker")
                    spfast("u colapse......")
                    spfast("%%%DDDDD%%%% %EEEEE% $$%$AAAAA&#$$%#(#TTTTT$&%# %^HHHHH$( 6( %")
                    spfast("")
                if win == True:
                    spfast("A rush of excitement courses through your body.")
                    spfast("You feel refreshed and powerful.")
                    spfast("What is thi-                       ")
                    time.sleep(3)
                    shining.stop()
                    winscreen()


            # player chooses blue door
            elif door_question in colorlist:
                door.play()
                spfast("You twist the rusty doorknob...")
                spfast("The door opens revealing pitch black darkness.")
                spfast("Something doesn't feel quite right...")
                door.stop()
                spfast("You're knocked on your feet by a strong force.")
                spfast("Everything goes black.")
                medieval.stop()
                print()
                die()
                death.play()
                print()
                    # message box for restart
                spfast("You have died...")
                time.sleep(1)
                titlescr()
                i += 1
                print("***************** GAME RESTARTED *****************")
                print("█ " + str(i) + "/3 attempts █")
                death.stop()
                medieval.play()
                continue

            else:
                medieval.stop()
                spfast("That's not an option.")
                death.play()
                spfast("You died for an being idiot.")
                titlescr()
                print("***************** GAME RESTARTED *****************")
                i += 1
                print("█ " + str(i) + "/3 attempts █")
                death.stop()
                medieval.play()
                continue

        elif q1 in nolist:
            spfast("Well... not quite")
            spfast("Let's try that again.")
            continue

        # if player fails first question
        else:
            medieval.stop()
            spfast("Yikes, you're a little dumb.")
            if q1 == "red":
                spfast("I asked if you could spell red, not to type it idiot.")
            death.play()
            spfast("You died on the first question...")
            spfast("Let's try that again.")
            time.sleep(.5)
            medieval.play()
            titlescr()
            i += 1
            print("***************** GAME RESTARTED *****************")
            print("█ " + str(i) + "/3 attempts █")
            death.stop()

    # lost the game - out of attempts
    else:
        spfast("Oops, looks like you are out of attempts.")
        spfast("Sorry but I gotta call it a wrap.")
        spfast("You really dropped the ball with this one " + name + ".")
        time.sleep(3)
        system('cls')
        medieval.stop()
        sadsong.play()
        print("    __         __      _________       ___      ___                ___            _________      _________    ____________  ")
        time.sleep(.1)
        print("   |  |       |  |    /         \     |   |    |   |              |   |          /         \    /    _____|  |            | ")
        time.sleep(.1)
        print("    |  |     |  |    |    ___    |    |   |    |   |              |   |         |    ___    |   |   /        |     _______| ")
        time.sleep(.1)
        print("     |  |   |  |     |   /   \   |    |   |    |   |              |   |         |   /   \   |   |  |         |    |         ")
        time.sleep(.1)
        print("      |  | |  |      |  |     |  |    |   |    |   |              |   |         |  |     |  |   |  \___      |    |_______  ")
        time.sleep(.1)
        print("       |    |        |  |     |  |    |   |    |   |              |   |         |  |     |  |    \___   \    |            | ")
        time.sleep(.1)
        print("        |  |         |  |     |  |    |   |    |   |              |   |         |  |     |  |         \  |   |     _______| ")
        time.sleep(.1)
        print("        |  |         |  |     |  |    |   |    |   |              |   |         |  |     |  |         |  |   |    |         ")
        time.sleep(.1)
        print("        |  |         |   \___/   |     \   \__/   /               |   |______   |   \___/   |    ___ /   |   |    |_______  ")
        time.sleep(.1)
        print("        |  |         |           |      \        /                |          |  |           |   /        |   |            | ")
        time.sleep(.1)
        print("        |__|          \_________/        \______/                 |__________|   \_________/    |_______/    |____________| ")
        time.sleep(2)
        print()
        print()
        for x in range(40):
            time.sleep(0.05)
            print("█", sep=' ', end='', flush=True)
        print()
        spfast("File deleted.")
        spfast("Good bye!")
        time.sleep(3)
        sys.exit()


main()





