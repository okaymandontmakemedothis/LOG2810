from PySimpleGUI import PySimpleGUI as sg
import usersettings
import os


#DEFAULT VALUES

def init():
	# global return_value
	# return_value = ""
	global data
	data = None
	global never_quit_filename_loop
	never_quit_filename_loop = True
	global choices
	choices = ["(a) Mettre a jour la carte.","(b) Determiner le plus court chemin securitaire.","(c) Extraire un sous-graphe.","(d) Quitter."]
	global reply
	reply="Opened program"
	global previous_reply
	previous_reply = ""
	global bye_art_path
	bye_art_path = os.path.expanduser(usersettings.absolute_path_to_working_directory+"images/ambulance2.gif")
	global program_name
	program_name = "Le Meilleur Programme du Monde"
	global default_menu_msg
	default_menu_msg = "Action precedente : "
	global default_layout_menu
	default_layout_menu = 	[
								[sg.Text(default_menu_msg, size=(40,1))],
								[sg.Button(button_text=choices[0], auto_size_button=True, pad=(1,1)), 
								sg.Button(button_text=choices[1], auto_size_button=True, pad=(1,1)), 
								sg.Button(button_text=choices[2], auto_size_button=True, pad=(1,1)), 
								sg.Button(button_text=choices[3], auto_size_button=True, pad=(1,1))]
							]



#THIS IS THE OUTPUT OF pprint(settings.data)
 # ['1,0\r\n',
 # '2,0\r\n',
 # '3,0\r\n',
 # '4,0\r\n',
 # '5,1\r\n',
 # '6,1\r\n',
 # '7,0\r\n',
 # '8,0\r\n',
 # '9,0\r\n',
 # '10,0\r\n',
 # '11,0\r\n',
 # '12,1\r\n',
 # '13,1\r\n',
 # '14,0\r\n',
 # '15,0\r\n',
 # '16,0\r\n',
 # '17,0\r\n',
 # '18,0\r\n',
 # '19,0\r\n',
 # '20,0\r\n',
 # '21,0\r\n',
 # '22,0\r\n',
 # '23,1\r\n',
 # '24,0\r\n',
 # '25,0\r\n',
 # '26,1\r\n',
 # '27,0\r\n',
 # '28,0\r\n',
 # '29,1\r\n',
 # '\r\n',
 # '1,2,18\r\n',
 # '1,22,20\r\n',
 # '1,24,19\r\n',
 # '1,25,17\r\n',
 # '1,26,19\r\n',
 # '2,3,23\r\n',
 # '2,7,24\r\n',
 # '2,19,16\r\n',
 # '3,4,23\r\n',
 # '3,7,19\r\n',
 # '3,17,20\r\n',
 # '3,19,16\r\n',
 # '3,21,28\r\n',
 # '4,5,23\r\n',
 # '4,9,23\r\n',
 # '4,17,19\r\n',
 # '4,21,23\r\n',
 # '5,6,19\r\n',
 # '5,9,21\r\n',
 # '5,17,28\r\n',
 # '6,9,20\r\n',
 # '6,18,23\r\n',
 # '6,29,16\r\n',
 # '7,8,17\r\n',
 # '7,16,20\r\n',
 # '7,19,16\r\n',
 # '7,26,17\r\n',
 # '8,11,19\r\n',
 # '8,13,20\r\n',
 # '8,16,18\r\n',
 # '8,19,15\r\n',
 # '9,10,27\r\n',
 # '9,20,28\r\n',
 # '9,21,29\r\n',
 # '9,29,17\r\n',
 # '10,28,19\r\n',
 # '10,29,16\r\n',
 # '11,13,18\r\n',
 # '11,17,19\r\n',
 # '11,18,17\r\n',
 # '11,19,15\r\n',
 # '12,13,16\r\n',
 # '12,15,17\r\n',
 # '12,18,16\r\n',
 # '12,29,15\r\n',
 # '13,15,16\r\n',
 # '13,16,17\r\n',
 # '14,15,17\r\n',
 # '14,16,16\r\n',
 # '15,16,16\r\n',
 # '16,25,19\r\n',
 # '16,26,18\r\n',
 # '17,18,17\r\n',
 # '17,19,15\r\n',
 # '18,29,14\r\n',
 # '20,21,20\r\n',
 # '22,23,19\r\n',
 # '22,24,18\r\n',
 # '23,24,18\r\n',
 # '24,25,17\r\n',
 # '25,26,19\r\n',
 # '27,28,15\r\n',
 # '27,29,16\r\n',
 # '28,29,14']
