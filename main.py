import settings
import usersettings
from creerGraphe import *
from gui import *
import os

#Users must update this part of the code with their own system settings
usersettings.init()
#Static settings
settings.init()

#First iteration

#Get some variables out here
g = None

#Display the menu for the first time
makeGUI()

#Further iterations
while 1:
	#Check first if the exit button has been pressed on
	if settings.reply == settings.choices[3]:
		msgbox("", image=os.path.expanduser(usersettings.absolute_path_to_working_directory+settings.bye_art))
		break
	#Then check the rest of the options
	if settings.reply == settings.choices[0]:
		g = lireGraphe()
	elif settings.reply == settings.choices[1]:
		pass
	elif settings.reply == settings.choices[2]:
		pass
	makeGUI()


