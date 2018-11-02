# from easygui import *
import settings
import usersettings
from PySimpleGUI import PySimpleGUI as sg
import os
from algo import *

class Gui:
	def __init__(self, title):
		self.title = title
		self.menu_message = settings.default_menu_msg
		self.layout = None
		self.window = None
		# self.return_value = None
		self.exit_status = False
		settings.previous_reply = settings.reply

		#Temp values
		self.output_token = None
		self.g=None
		self.output_block = None
		self.payload = None



	def updateG(self, g):
		self.g = g

	def setOutputBlock(self, output_block):
		self.output_block = output_block

	def setOutputToken(self, output_token):
		self.output_token = output_token
		
	def setLayoutMenuDefault(self):
		self.layout = settings.default_layout_menu

	def updateLayoutMenu(self, output_block):
		self.layout = 	[
							[sg.Text(self.menu_message, size=(40,1))],
							output_block if output_block is not None else [sg.Text(text="")],
							[sg.Button(button_text=settings.choices[0], auto_size_button=True, pad=(1,1)), 
							sg.Button(button_text=settings.choices[1], auto_size_button=True, pad=(1,1)), 
							sg.Button(button_text=settings.choices[2], auto_size_button=True, pad=(1,1)), 
							sg.Button(button_text=settings.choices[3], auto_size_button=True, pad=(1,1))]

						]

	def makeGUI(self):
		while all(settings.reply != choice for choice in settings.choices) :
			#fonction to update message with previous action at the top
			self.menu_message += settings.previous_reply
			self.updateLayoutMenu(self.output_block)

			#GUI call
			# settings.reply = buttonbox(message, title=title, image=graphImage, choices=settings.choices)

			self.window = sg.Window(self.title).Layout(self.layout).Finalize()
			#Used the output_block once, now delete it
			self.output_block=None
			#Due to the shitty Nature of this GUI I need to print the STDOUTs immediately after creating this menu.
			if self.output_token == 0:
				GrapheImpression = lireGraphe(self.g.getNodes())
				print(f"{GrapheImpression}")
				self.window.Refresh()
			if self.output_token == 1:
				plusCourtChemin(self.g, self.askC3())
				self.window.Refresh()
			if self.output_token == 2:
				payload = self.askC4()
				from pprint import pprint 
				pprint(payload)
			#Read values therefore this is like a while until it reads something nothing will execute before this is done
			settings.reply, value = self.window.Read()

			#In case red button quit or cmd-q
			if settings.reply is None:
				settings.reply = ""
				self.exit_status = True
				self.window.Close()
				break

			#reset the message value
			self.menu_message = self.menu_message.replace(settings.previous_reply, "")

			#update previous_reply with reply because this is when you dont need the previous reply anymore
			settings.previous_reply = settings.reply

	def makeReplyGUI(self, g):
		# if settings.reply == settings.choices[0] :
		# 	pass
		# elif settings.reply == settings.choices[1] :

		# 	pass
		# elif settings.reply == settings.choices[2] :
			
		# 	pass
		# elif settings.reply == settings.choices[3] :
		if settings.reply == settings.choices[3] :
			#this is the extent of this GUI framework. no resizing stuff. welp. and gotta hardcode to pixels for windows/images boxes and character length for text/buttons boxes
			layout_bye=	[
				[sg.Text("Bye!",size=(132,1),justification='center', pad=(1,1))],
				[sg.Image(filename=settings.bye_art_path, size=(800,600),pad=(1,1))],
				[sg.Exit(size=(132,1))]
			]	
			while(1):
				self.window = sg.Window(self.title, default_element_size=(30,1)).Layout(layout_bye)
				event, value = self.window.Read()
				if event == "Exit" or event is None :
					self.exit_status = True
					break

	def askFileNameGUI(self):
		layout = 	[
						[sg.Text(text="Enter the name of the file : ")],
						[sg.InputText("")],
						[sg.ReadButton('Read', bind_return_key=True)]
					]
		ask_box = sg.Window(settings.program_name, return_keyboard_events=True, use_default_focus=False).Layout(layout)
		while(True):
			event, value = ask_box.Read()
			if event is 'Read':
				stripped_reply = value[0].replace(" ","").split('.')
				if len(stripped_reply)==2:
					if(stripped_reply[1]=='txt'):
						ask_box.Close()
						return stripped_reply[0]+'.'+stripped_reply[1]
				elif len(stripped_reply)==1:
					ask_box.Close()
					return stripped_reply[0]+".txt"
				else: 
					ask_box.Close()
					raise IOError(stripped_reply)

	def askC3(self):
		layout = 	[
						[sg.Text(text="Choissisez la severite du patient a risque")],
						[sg.InputCombo(['Patient à faible risque', 'Patient à moyen risque', 'Patient à haut risque'])],
						[sg.Text(text="Choissisez le point de depart")],
						[sg.InputCombo([i for i in range(1,len(self.g.getNodes())+1)])],
						[sg.Text(text="Choissisez le point d'arrivee")],
						[sg.InputCombo([i for i in range(1,len(self.g.getNodes())+1)])],
						[sg.Submit()]
					]
		window = sg.Window(self.title).Layout(layout).Finalize()

		while(True):
			event, value = window.Read()
			if event is not None:
				payload = Payload(typePatient=value[0], start_index=self.g.getNode(int(value[1])), end_index=self.g.getNode(int(value[2])))
				window.Close()
				return payload

	def askC4(self):
		layout = 	[
						[sg.Text(text="Choissisez le type de voiture")],
						[sg.InputCombo(['NI-NH', 'LI-ion'])],
						[sg.Text(text="Choissisez le point de depart")],
						[sg.InputCombo([i for i in range(1,len(self.g.getNodes())+1)])],
						[sg.Submit()]
					]
		window = sg.Window(self.title).Layout(layout).Finalize()

		while(True):
			event, value = window.Read()
			if event is not None:
				payload = Payload(typePatient=value[0], start_index=self.g.getNode(int(value[1])), end_index=None)
				window.Close()
				return payload

	def makeErrorGUI(self, title="Error!", message="An error has occured."):
		error_window = sg.Window(title).Layout([
								[sg.Text(message, auto_size_text=True, pad=(1,1))],
								[sg.OK(pad=(1,1))]
							])
		while(True):
			event, value = error_window.Read()
			if event == "OK" or event is None :
				error_window.Close()
				break
