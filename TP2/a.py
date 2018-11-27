from pynput import keyboard
from time import sleep

global keyCapture
keyCapture = ""

def hasChanged(word):
	pass

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

logger = keyboard.Listener(on_release=on_release)
logger.start()
	

word = ""
while True :
	#guess to not spam the program
    sleep(0.1)
    print(keyCapture," released")
    #add the keyCapture to our string
    if keyCapture == 'Key.backspaceKey.backspace':
    	word = 
    word += "{0}".format(keyCapture)
    #reset the keyCapture before it appends forever for just staying still
    keyCapture = ""
    #constantly take off the annoying apostrophes
    word = word.replace("'","")
    print(word)
    if hasChanged(word):
    	pass
    	#call the algorithm function here

print("Stopping Keylogger")
logger.stop()


# s/o to this https://github.com/cbrafter/CrowdTLL/blob/master/generalCode/keyTest.py
# NOTE: il serait interessant d'ajouter le support de backspace
