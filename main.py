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
	try:
		gui.makeGUI()
		#Then check the rest of the options
		if settings.reply == settings.choices[0]:	
			g = creerGraphe(gui.askFileNameGUI())
			if g is not None:
				#print to gui
				layout = 	[	
								#size of the main menu that we have to tatonner coz of this framework..
								[sg.Output(size=(87,20))]
							]
				new_window = sg.Window("Test graphe output").Layout(layout).Finalize()
				g.printGraphe()
				new_window.Refresh()
				while(True):
					event, value = new_window.Read()
					if event is None:
						break
		elif settings.reply == settings.choices[1]:
			pass
		elif settings.reply == settings.choices[2]:
			pass
		gui.makeReplyGUI(g)
		if gui.exit_status is True: 
			break
		settings.reply = ""
	except IOError as e:
		print(type(e.args[0]))
		if type(e.args[0]) is list:
			gui.makeErrorGUI(message="IOError - An unexpected filename was entered: {0}".format(e))
			g = None
		else:
			gui.makeErrorGUI(message="{0}".format(e))
			g =  None

