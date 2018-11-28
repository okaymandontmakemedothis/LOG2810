#!/usr/bin/env python
# -*- coding: latin-1 -*-
from pynput import keyboard
from time import sleep
import asyncio
from trie import *
import re


global keyCapture
keyCapture = ""

def hasChanged(word, previous_word):
    if previous_word == word:
        return False
    else: 
        return True

async def wordPrint(word, previous_word, root):
    if hasChanged(word, previous_word):
        #call the algorithm function here
        try:
            wordlist = findWord(root, word)
            print()
            print("Mot courant : " ,word)
            for w in wordlist:
                print(w)
        except Exception as e:
            print()
            print("Mot courant : " ,word)
            print("Erreur : Le mot n'existe pas")


def on_press(key):
	global keyCapture
	try:
		pass
	except AttributeError:
		print('special key {0} pressed'.format(
            key))

def on_release(key):
    global keyCapture
    keyCapture = '{0}'.format(key)

# Collect events until released
async def main():
    pattern = re.compile("\D{1}")
    global keyCapture
    keyCapture = ""
    root = TrieNode("", None)
    readDictionnary(root, "./lexique1.txt")
    logger = keyboard.Listener(on_release=on_release)
    logger.start()
    	

    word = ""
    while True :
        previous_word = word
    	#guess to not spam the program
        sleep(0.1)
        # print(keyCapture," released")
        # print(type(keyCapture))
        # print(keyCapture)
        # add the keyCapture to our string
        # import pdb; pdb.set_trace()
        capture = "{0}".format(keyCapture)
        if capture == "Key.backspace":
            keyCapture = ""
            word = word[:-1]
        elif pattern.match(capture):
            pass
            # word += "{0}".format(keyCapture)
        word += "{0}".format(keyCapture)
        #reset the keyCapture before it appends forever for just staying still
        keyCapture = ""
        #constantly take off the annoying apostrophes
        word = word.replace("'","")
        await wordPrint(word, previous_word, root)

    # print("Stopping Keylogger")
    # logger.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
# s/o to this https://github.com/cbrafter/CrowdTLL/blob/master/generalCode/keyTest.py
