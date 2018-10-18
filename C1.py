import os
from pprint import pprint
from C5 import *
import usersettings
import settings

def creerGraph():
	try:
		name = askFileName()
		with open(os.path.expanduser(usersettings.absolute_path_to_working_directory+name), 'r') as file:
			settings.never_quit_filename_loop = False
			settings.data=file.readlines()
			pprint(settings.data)
			#This works. It is an array as suspected and not a list. Apparently it is a list....https://www.w3schools.com/python/python_lists.asp
			pprint(settings.data[0])
	except IOError:
		print("IOError: A non existent filename was entered = " + name)

	#Trying to put data into a 2D array
	settings.data
	return
