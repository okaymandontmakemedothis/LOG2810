#!/usr/bin/env python
from pynput import keyboard
from time import sleep
import asyncio
from trie import *
import re
import sys

global keyCapture
keyCapture = ""
global word_count

def hasChanged(word, previous_word):
    if previous_word == word:
        return False
    else: 
        return True

async def wordPrint(word, previous_word, root):
    if hasChanged(word, previous_word):
        #call the algorithm function here
        global word_count
        try:
            wordlist = findWord(root, word)
            word_count = len(wordlist)
            print()
            print("Mot courant : " ,word)
            for w in wordlist:
                print(w)
        except Exception as e:
            print()
            print("Mot courant : " ,word)
            print("Erreur : Le mot n'existe pas")


def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

def flushResults(lines):
    for line in range(lines):
        delete_last_line()

def on_press(key):
	global keyCapture
	try:
		pass
	except AttributeError:
		print('special key {0} pressed'.format(key))

def on_release(key):
    global keyCapture 
    keyCapture = '{0}'.format(key) 

# Collect events until released
async def main():
    allow = False
    pattern = re.compile("\D{1}")
    global keyCapture
    keyCapture = ""
    global word_count
    word_count = 0
    root = TrieNode("", None)
    if sys.argv:
        for arg in sys.argv[1:]:
            if arg == "-h":
                print()
                print("NAME")
                print("\tTP2.py")
                print()
                print("SYNOPSIS")
                print("\tpython3 TP2.py [-l] source_lexique ...")
                print("\tpython3 TP2.py [-h]")
                print()
                print("DESCRIPTION")
                print("\t1-Cree une Trie a partir d'un fichier lexique voulu.")
                print("\t2-Permet a l'usager de rechercher un mot voulu")
                print("\t3-Compte de mots valides tapes et ce, sur commande")
                print()
            elif arg == "-l":
                for lexique in sys.argv[2:]:
                    # print(lexique)
                    readDictionnary(root, "./"+lexique)
                allow = True
                break
            else:
                print("Did you mean \"-h\"?")

        if allow:
            logger = keyboard.Listener(on_release=on_release)
            logger.start()
                

            word = ""
            while True :
                previous_word = word
                #guess to not spam the program
                sleep(0.1)
                capture = "{0}".format(keyCapture)
                if capture == "Key.backspace":
                    keyCapture = ""
                    word = word[:-1]
                elif pattern.match(capture) and len(keyCapture)==3:
                    # print("added something!")
                    word += "{0}".format(keyCapture)
                else:
                    if keyCapture == "Key.space" or "Key.tab" or "Key.enter" or "Key.shift" or "Key.cmd": 
                        keyCapture = ""
                #reset the keyCapture before it appends forever for just staying still
                keyCapture = ""
                #constantly take off the annoying apostrophes
                word = word.replace("'","")
                flushResults(word_count+1)
                await wordPrint(word, previous_word, root)

    else:
        print("Did you mean -h?")

    # print("Stopping Keylogger")
    # logger.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
# s/o to this https://github.com/cbrafter/CrowdTLL/blob/master/generalCode/keyTest.py
