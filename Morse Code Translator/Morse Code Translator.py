import os
from os import system
import sys
import time

MORSE_CODE_DICT = { 'A' : '.-', 'B':'-...',
                    'C' : '-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
MORSE_TO_PLAIN = { '.-' : 'A', '-...':'B',
                    '-.-.' : 'C', '-..':'D', '.':'E',
                    '..-.':'F', '--.':'G', '....':'H',
                    '..':'I', '.---':'J', '-.-':'K',
                    '.-..':'L', '--':'M', '-.':'N',
                    '---':'O', '.--.':'P', '--.-':'Q',
                    '.-.':'R', '...':'S', '-':'T',
                    '..-':'U', '...-':'V', '.--':'W',
                    '-..-':'X', '-.--':'Y', '--..':'Z',
                    '.----':'1', '..---':'2', '...--':'3',
                    '....-':'4', '.....':'5', '-....':'6',
                    '--...':'7', '---..':'8', '----.':'9',
                    '-----':'0', '--..-- ':', ', '.-.-.-':'.',
                    '..--..':'?', '-..-.':'/', '-....-':'-',
                    '-.--.':'(', '-.--.-':')'}


def titlescr():
    print(r"""
     __    __    ______    ______    ______    ______       ______   ______    ______    __   __    ______    __        ______    ______   ______    ______    
    /\ "-./  \  /\  __ \  /\  == \  /\  ___\  /\  ___\     /\__  _\ /\  == \  /\  __ \  /\ "-.\ \  /\  ___\  /\ \      /\  __ \  /\__  _\ /\  __ \  /\  == \   
    \ \ \-./\ \ \ \ \/\ \ \ \  __<  \ \___  \ \ \  __\     \/_/\ \/ \ \  __<  \ \  __ \ \ \ \-.  \ \ \___  \ \ \ \____ \ \  __ \ \/_/\ \/ \ \ \/\ \ \ \  __<   
     \ \_\ \ \_\ \ \_____\ \ \_\ \_\ \/\_____\ \ \_____\      \ \_\  \ \_\ \_\ \ \_\ \_\ \ \_\\"\_\ \/\_____\ \ \_____\ \ \_\ \_\   \ \_\  \ \_____\ \ \_\ \_\ 
      \/_/  \/_/  \/_____/  \/_/ /_/  \/_____/  \/_____/       \/_/   \/_/ /_/  \/_/\/_/  \/_/ \/_/  \/_____/  \/_____/  \/_/\/_/    \/_/   \/_____/  \/_/ /_/ 
                                                                                                                                                                                                                                                                                       
                                                                    A Simple Morse and Text Converter - Gnatt
                                                                    
    """)

titlescr()


def Morse_Translator(code):
    result = ""
    for letter in code:
        result = result + MORSE_CODE_DICT[letter] + "|"
    return result


def Reverse_Translator(reverse):
    return ''.join(MORSE_TO_PLAIN.get(i) for i in reverse.split())


def translator_prompt():
    quit = False
    while quit is False:
        try:
            print(Morse_Translator(input("What to Convert?: ").upper()))
            quit1 = input("Type \"exit\" to go back. Press ENTER to else to keep converting: ")
            if quit1 == "exit":
                PROGRAMM()
            else:
                translator_prompt()
        except:
            print("Invalid Function")
            time.sleep(.3)


def reverse_trans():
    quit = False
    while quit is False:
        try:
            print(Reverse_Translator(input("What to Convert?: ").upper()))
            quit2 = input("Type \"exit\" to go back. Press ENTER to else to keep converting: ")
            if quit2 == "exit":
                PROGRAMM()
            else:
                reverse_trans()
        except:
            print("Invalid Function")
            time.sleep(.3)


def PROGRAMM():
    PROGRAM = input("TEXT TO MORSE(1) | MORSE TO TEXT(2): ")
    if PROGRAM == "1":
        system('cls')
        titlescr()
        print("TEXT TO MORSE")
        print()
        print("\"Characters are separated with a \"|\"")
        print("Do not put spaces between words.")
        time.sleep(.3)
        print()
        translator_prompt()
    elif PROGRAM == "2":
        system('cls')
        titlescr()
        print("MORSE TO TEXT")
        print()
        print("Put a space at the end of each morse code block.")
        time.sleep(.3)
        print()
        reverse_trans()
    else:
        print("Invalid Operation")
        time.sleep(1)
        PROGRAMM()



PROGRAMM()