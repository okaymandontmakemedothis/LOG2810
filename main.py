import settings
import usersettings
from creerGraphe import *
from gui import *


#Users must update this part of the code with their own system settings
usersettings.init()
#Static settings
settings.init()

#First iteration

#Get some variables out here
g = None
gui=Gui(settings.program_name)

#Display the menu for the first time


#Further iterations
while 1:
	gui.makeGUI()
	#Check first if the exit button has been pressed on
	if settings.reply == settings.choices[3]:
		pass
	#Then check the rest of the options
	if settings.reply == settings.choices[0]:
		try:
			g = creerGraphe(gui.askFileNameGUI())
			if g is not None:
				g.printGraphe()
		except IOError as e:
			print(type(e.args[0]))
			if type(e.args[0]) is list:
				gui.makeErrorGUI(message="IOError - An unexpected filename was entered: {0}".format(e))
				return None
			else:
				gui.makeErrorGUI(message="{0}".format(e))
				return None
	elif settings.reply == settings.choices[1]:
		pass
	elif settings.reply == settings.choices[2]:
		pass
	gui.makeReplyGUI(g)
	if gui.exit_status is True: 
		break


