import os
import pprint

def creerGraph():
	try:
		name = askFileName()
		with open(os.path.expanduser(usersettings.absolute_path_to_working_directory+name), 'r') as file:
			settings.never_quit_filename_loop = False
			settings.data=file.readlines()
			pprint(settings.data)
	except IOError:
		print("IOError: A non existent filename was entered = " + name)

	return
