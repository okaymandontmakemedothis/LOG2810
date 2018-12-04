#!/usr/bin/env python
from pynput import keyboard
from time import sleep
import asyncio
from trie import *
import re
import sys
import pprint

keyCapture = ""
permanent_wordlist = list()
history = list()

def readDictionnary(root, fileName):
    with open(  fileName, 'rU', encoding='latin-1') as f:
        for line in f.readlines():
            a = line.split()
            insertWord(root, a[0])

def hasChanged(word, previous_word):
    if previous_word == word:
        return False
    else: 
        return True

async def wordPrint(word, previous_word, root):
    if hasChanged(word, previous_word):
        global wordlist
        try:
            wordlist = findWord(root, word)
            word_count = len(wordlist)
            print()
            print("Mot courant : " ,word)
            for w in wordlist:
                a,b = w
                # print(a," (",b,")")
                print(a)
        except Exception as e:
            print()
            print("Mot courant : " ,word)
            print("Erreur : Le mot n'existe pas")
    else:
        pass

def updatePermWordlist():
    global permanent_wordlist
    global wordlist
    global history
    for w in wordlist:
        a,b = w
        if b == 0 :
            pass
        else:
            if w not in history:
                history.append(w)
            w_old = (a, b-1) 
            if w_old in permanent_wordlist:
            #update the value
                permanent_wordlist.remove( w_old )
            elif w in permanent_wordlist:
                pass
            else:
                permanent_wordlist.append(w)
    # print(history)


async def countPrint():
    global permanent_wordlist
    global history
    temp_history = list() + history
    for i,w in enumerate(history[::-1]):
        a,b = w
        count = 0
        print("word", w)
        for w_rem in (temp_history[::-1])[i:]:
            print("Print:",w_rem)
            if a in w_rem:
                if count == 0:
                    pass
                else:
                    temp_history.remove(w_rem)
            count+=1

    #oldest to newest 
    for w in temp_history:
        print(w)
    # for index, w in enumerate(temp_history):
    #     temp = w[0]
    #     i = index
    #     if i+1 < len(temp_history):
    #         while temp in temp_history[i+1] and i+1 < len(temp_history):
    #             temp_history.remove(temp_history[i+1])
    #             i+=1
    # for i in temp_history:
    #     print(i)

    for w in permanent_wordlist:
        a,b = w
        recent_index = 0
        for wth in temp_history:
            if a in wth:
                recent_index = 1
        print()
        print(a, " (", b, ") ", "(", recent_index, ") ")
        # if len(permanent_wordlist) <= 5:
        #     print()
        #     print(a," (",b,")", "(",1,")")
        # else:
        #     if index < len(permanent_wordlist)-5:
        #         print()
        #         print(a," (",b,")", "(",0,")")
        #     else:
        #         print()
        #         print(a," (",b,")", "(",1,")")



def scanWordlist():
    global permanent_wordlist


            

def on_release(key):
    global keyCapture 
    keyCapture = '{0}'.format(key) 

# Collect events until released
async def main():
    allow = False
    token = True
    pattern = re.compile("\D{1}")
    global keyCapture
    keyCapture = ""
    global wordlist
    wordlist = list()
    root = TrieNode("", None)
    if sys.argv:
        for arg in sys.argv[1:]:
            if arg == "-h":
                print()
                print("NAME")
                print("\tTP2.py")
                print()
                print("SYNOPSIS")
                print("\tpython3 TP2.py [-l] source_lexique ... [options]")
                print("\tpython3 TP2.py [-h]")
                print()
                print("DESCRIPTION")
                print("\t1-Cree une Trie a partir d'un fichier lexique voulu.")
                print("\t2-Permet a l'usager de rechercher un mot voulu")
                print("\t3-Compte de mots valides tapes et ce, sur commande")
                print()
                print("The options are as follows:")
                print("\t-\tDisplays how many time each word in the dictionnary has been entirely written by the user")
                print()
            elif arg == "-l":
                for lexique in sys.argv[2:]:
                    print(lexique, "a ete bien ajoute.")

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
                    token = True
                    updatePermWordlist()
                elif pattern.match(capture) and len(keyCapture)==3:
                    # print("added something!")
                    word += "{0}".format(keyCapture)
                    token = True
                    updatePermWordlist()
                elif "-" in word and token:
                    #Whatever it still searches this in trie... I wish the input was awaitable in some ways but no the listener has to listen to anything and everything
                    #def print count
                    updatePermWordlist()
                    await countPrint()
                    #erase the -
                    word = word[:-1]
                    token = False
                else:
                    if keyCapture == "Key.space" or "Key.tab" or "Key.enter" or "Key.shift" or "Key.cmd": 
                        keyCapture = ""
                #reset the keyCapture before it appends forever for just staying still
                keyCapture = ""
                #constantly take off the annoying apostrophes
                word = word.replace("'","")
                if token:
                    await wordPrint(word, previous_word, root)
    else:
        print("Did you mean -h?")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
# s/o to this https://github.com/cbrafter/CrowdTLL/blob/master/generalCode/keyTest.py
