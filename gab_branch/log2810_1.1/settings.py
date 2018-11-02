from PySimpleGUI import PySimpleGUI as sg
import usersettings
import os


#DEFAULT VALUES

def init():

#UI IMAGES	

	global bye_art_path
	bye_art_path = os.path.expanduser(usersettings.absolute_path_to_working_directory+"images/ambulance2.gif")
	
#UI TEXT

	global program_name
	program_name = "Le Meilleur Programme du Monde"
	global default_menu_msg
	default_menu_msg = "Action precedente : "
	global reply
	reply="Opened program"
	global previous_reply
	previous_reply = ""
	global choices
	choices = ["(a) Mettre a jour la carte.","(b) Determiner le plus court chemin securitaire.","(c) Extraire un sous-graphe.","(d) Quitter."]


#UI SIZES

	global default_layout_menu
	default_layout_menu = 	[
								[sg.Text(default_menu_msg, size=(40,1))],
								[sg.Button(button_text=choices[0], auto_size_button=True, pad=(1,1)), 
								sg.Button(button_text=choices[1], auto_size_button=True, pad=(1,1)), 
								sg.Button(button_text=choices[2], auto_size_button=True, pad=(1,1)), 
								sg.Button(button_text=choices[3], auto_size_button=True, pad=(1,1))]
							]
	global layout_stdout_output
	layout_stdout_output = [sg.Output(size=(87,20))]
	global layout_patient_type
	layout_patient_type = [[sg.InputCombo(['Transport à faible risque', 'Transport à moyen risque', 'Transport à haut risque'])]]


#UI LOGIC

	global output_token_values
	output_token_values = [0,1,2]
