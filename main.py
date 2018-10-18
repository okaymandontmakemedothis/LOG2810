import settings
import usersettings
from C1 import *
from C5 import *
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
	if settings.return_value == settings.choices[0]:
		while 1:
			creerGraph()
			settings.return_value = ""
			# if x: break
			break
		#
		# makeGUI()
	else:
		#Should be passing a graphImage
		makeGUI()

	if settings.return_value == settings.choices[1]:
		pass
	else:
		makeGUI()

	if settings.return_value == settings.choices[2]:
		pass
	else:
		makeGUI()

	if settings.return_value == settings.choices[3]:
		msgbox("", image=os.path.expanduser(usersettings.absolute_path_to_working_directory+settings.bye_art))
		break
