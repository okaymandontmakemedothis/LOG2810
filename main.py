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

#test- it works... credits: https://stackoverflow.com/a/41211614
# import os
# print (os.getcwd())
# with open(os.path.expanduser("~/Downloads/session3/LOG2810/centresLocaux.txt"), "r") as f:
# 	print("yay")


#Further iterations
while 1:
	if settings.return_value == settings.choices[0]:
		print("we entered here!...")
		while settings.never_quit_filename_loop:
			try:
				name = askFileName()
				with open(os.path.expanduser(usersettings.absolute_path_to_working_directory+name), 'r') as file:
					settings.never_quit_filename_loop = False
					settings.data=file.readlines()

			except IOError:
				print("IOError: A non existent filename was entered = " + name)

		#
		makeGUI()
	else:
		print("we didn't enter there")
		msgbox("hello")
		break
