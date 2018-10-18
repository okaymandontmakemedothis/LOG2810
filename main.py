import settings
from C1 import *
from C5 import *

settings.init()

data = None

#First iteration

#Display the menu for the first time
makeGUI()

#Further iterations
while 1:
	if settings.return_value == choices[0]:
		print("we entered here!...")
		with open(askFileName(), 'r') as file:
			data=file.readlines()
		#
		makeGUI()
	else:
		print("we didn't enter there")
		msgbox("hello")
		break
