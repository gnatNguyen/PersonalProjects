import os
import time
import playsound as ps
import speech_recognition as sr
from gtts import gTTS
from pynput.keyboard import Key, Controller as keyboardController

k = keyboardController()

# simulates normal human typing
def type(output_text):
	time.sleep(.5)
	for x in output_text:
		k.type(x)
		time.sleep(.05)

# uses robot voice to speak a string
def speak(text):
	tts = gTTS(text=text, lang='en')
	filename = "clip.mp3"
	tts.save(filename)
	ps.playsound(filename)
	os.remove("clip.mp3")

# recieves audio from the micro phone and returns it as a string
def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)

		said = ""

		try:
			said = r.recognize_google(audio)
			
		except Exception as e:
			speak("I didn't understand")
	return said

# dictionary that contains punctuation and its counterpart
punctuations = {"period": ". ", "comma": ", ", "question mark": "? ", "exclamation": "! "}

writeWord = "type"

# calls the function to get audio input and outputs it to a variable
spoken_text = get_audio()

# loop that keeps running until user says to quit
while "quit" not in spoken_text:

	# turns the string into lowercase
	spoken_text = spoken_text.lower()

	# this checks to see if user wants to open an application
	if "open" in spoken_text and writeWord not in spoken_text:
		# splits each word from the input string to a list
		open_app = list(spoken_text.split(" "))

		# this removes the word "open" from the list
		for x in open_app:
			if x == "open":
				open_app.remove(x)

		# the list is put back together into a string
		output_text = ' '.join(open_app)

		# presses window key and types in the application wanted
		k.press(Key.cmd)
		k.release(Key.cmd)
		time.sleep(.5)
		k.type(output_text)
		time.sleep(.5)
		k.press(Key.enter)
		k.release(Key.enter)

	elif writeWord in spoken_text:
		list_words = list(spoken_text.split(" "))
		for n, x in enumerate(list_words):
			if x.lower() == writeWord:
				list_words.remove(x)
			if x in punctuations:
				list_words[n] = punctuations[n]
			if x == "i":
				list_words[n] = "I"

		list_words[0] = list_words[0].capitalize()
		output_text = ' '.join(list_words)

		type(output_text + " ")

	elif "search" in spoken_text:
		k.press(Key.cmd)
		k.release(Key.cmd)
		time.sleep(.5)
		k.type("chrome")
		time.sleep(.5)
		k.press(Key.enter)
		k.release(Key.enter)

		list_words = list(spoken_text.split(" "))
		for x in list_words:
			if x == "search":
				list_words.remove(x)
		output_text = ' '.join(list_words)
		type(output_text)
		k.press(Key.enter)
		time.sleep(.05)
		k.release(Key.enter)

	elif "switch application" in spoken_text:
		k.press(Key.alt)
		time.sleep(.2)
		k.press(Key.tab)
		time.sleep(.2)
		k.release(Key.alt)
		k.release(Key.tab)

	elif "save application" in spoken_text:
		k.press(Key.ctrl)
		time.sleep(.05)
		k.type("s")
		time.sleep(.05)
		k.release(Key.ctrl)
		time.sleep(.05)
		k.type("fileSave")
		k.press(Key.enter)
		k.release(Key.enter)

	elif "close application" in spoken_text:
		k.press(Key.ctrl)
		time.sleep(.05)
		k.type("w")
		time.sleep(.05)
		k.release(Key.ctrl)

	elif "shut down my computer" in spoken_text:
		speak("Goodbye gamer, don't go for too long, I will miss you.")
		time.sleep(.5)
		os.system("shutdown /s /t 5")


	spoken_text = get_audio()

speak("Goodbye fellow gamer")

exit()

	
