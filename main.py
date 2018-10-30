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

#Display the menu for the first time
makeGUI()

#Further iterations
while 1:
	#Check first if the exit button has been pressed on
	if settings.return_value == settings.choices[3]:
		msgbox("", image=os.path.expanduser(usersettings.absolute_path_to_working_directory+settings.bye_art))
		break
	#Then check the rest of the options
	if settings.return_value == settings.choices[0]:
		g = lireGraphe();
		# settings.return_value = "" # this is to reset the return_value if we ever want to use it... but it promotes bad practices...
	elif settings.return_value == settings.choices[1]:
		pass
	elif settings.return_value == settings.choices[2]:
		pass
	makeGUI()


