from pynput.keyboard import Key, Controller as keyboardController
from pynput.mouse import Button, Controller as mouseController
import time

#set ups mouse and keyboard
m = mouseController()
k = keyboardController()

#opens windows and searches for idle
k.press(Key.cmd)
k.release(Key.cmd)
time.sleep(.3)
k.type("idle")
time.sleep(.2)
k.press(Key.enter)
k.release(Key.enter)
time.sleep(2)

#opens a new file
k.press(Key.ctrl)
k.press("n")
k.release(Key.ctrl)
k.release("n")
time.sleep(.5)

#imports modules to run shit
k.type("from pynput.keyboard import Key, Controller as keyboardController")
k.press(Key.enter)
k.release(Key.enter)
time.sleep(.5)
k.type("import time")
k.press(Key.enter)
k.release(Key.enter)
time.sleep(.5)
k.type("import sys")
k.press(Key.enter)
k.release(Key.enter)
time.sleep(.5)

""" NEW SCRIPT BEING WRITTEN """
time.sleep(1.3)
worrds = "k = keyboardController()|k.press(Key.cmd)|k.release(Key.cmd)|time.sleep(.3)|k.type(\"idle\")|time.sleep(.2)|k.press(Key.enter)|k.release(Key.enter)|time.sleep(1.2)"
for letter in worrds:
    end = ""
    if letter == "|":
        end = end + ""
        k.press(Key.enter)
        k.release(Key.enter)
    else:
        end = end + letter
        k.press(end)
        k.release(end)
        time.sleep(.03)

k.press(Key.enter)
k.release(Key.enter)

worrrrrddsss = "words = 'print(\"Hello World\")'|for letter in words:|k.press(letter)|k.release(letter)|time.sleep(.15)"
for letter in worrrrrddsss:
    end = ""
    if letter == "|":
        end = end + ""
        k.press(Key.enter)
        k.release(Key.enter)
    else:
        end = end + letter
        k.press(end)
        k.release(end)
        time.sleep(.03)

k.press(Key.enter)
k.release(Key.enter)
k.press(Key.backspace)
k.release(Key.backspace)

words3 = "time.sleep(.5)|k.press(Key.enter)|k.release(Key.enter)|time.sleep(.5)|words2 = 'exit()'|for letter in words2:|k.press(letter)|k.release(letter)|time.sleep(.2)"
for letter in words3:
    end = ""
    if letter == "|":
        end = end + ""
        k.press(Key.enter)
        k.release(Key.enter)
    else:
        end = end + letter
        k.press(end)
        k.release(end)
        time.sleep(.03)

k.press(Key.enter)
k.release(Key.enter)
k.press(Key.backspace)
k.release(Key.backspace)

words4 = "time.sleep(1)|k.press(Key.enter)|k.release(Key.enter)|time.sleep(1)|k.press(Key.enter)|k.release(Key.enter)"
for letter in words4:
    end = ""
    if letter == "|":
        end = end + ""
        k.press(Key.enter)
        k.release(Key.enter)
    else:
        end = end + letter
        k.press(end)
        k.release(end)
        time.sleep(.03)

k.press(Key.ctrl)
k.press(Key.shift)
k.press("s")
k.release(Key.ctrl)
k.release(Key.shift)
k.release("s")

time.sleep(2)

k.type("Soon to be Sentient")

time.sleep(2)

k.press(Key.enter)
k.release(Key.enter)

time.sleep(1)

k.press(Key.f5)
k.release(Key.f5)




