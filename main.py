import settings
import usersettings
from C1 import *
from C5 import *

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
		while 1:
			creerGraph()
			# if x: break
			break
		#
		# makeGUI()
	else:
		print("we didn't enter there")
		msgbox("hello")
		break
