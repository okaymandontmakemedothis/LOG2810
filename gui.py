# from easygui import *
import settings
import usersettings
from PySimpleGUI import PySimpleGUI as sg
import os


class Gui:
	def __init__(self, title, g):
		self.title = title
		self.menu_message = settings.default_menu_msg
		self.layout = None
		self.window = None
		# self.return_value = None
		self.exit_status = False
		settings.previous_reply = settings.reply

		#Temp values
		self.output_token = None
		self.g=g
		self.output_block = None



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
			self.menu_message += settings.reply
			self.updateLayoutMenu(self.output_block)

			#GUI call
			# settings.reply = buttonbox(message, title=title, image=graphImage, choices=settings.choices)

			self.window = sg.Window(self.title).Layout(self.layout).Finalize()
			#Used the output_block once, now delete it
			self.output_block=None
			#Due to the shitty Nature of this GUI I need to print the STDOUTs immediately after creating this menu.
			if self.output_token==0:
				self.g.printGraphe()
				self.window.Refresh()


			#Read values therefore this is like a while until it reads something nothing will execute before this is done
			settings.reply, value = self.window.Read()
			print(settings.reply)




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
		self.window.Finalize()
		self.window.Close()
		if settings.reply == settings.choices[0] :
			pass
		elif settings.reply == settings.choices[1] :

			pass
		elif settings.reply == settings.choices[2] :
			
			pass
		elif settings.reply == settings.choices[3] :
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
				print(value[0])
				print(type(value[0]))
				stripped_reply = value[0].replace(" ","").split('.')
				if len(stripped_reply)==2:
					if(stripped_reply[1]=='txt'):
						ask_box.Close()
						print(".txt is not needed")
						return stripped_reply[0]+'.'+stripped_reply[1]
				elif len(stripped_reply)==1:
					ask_box.Close()
					print(".txt has been added")
					return stripped_reply[0]+".txt"
				else: 
					raise IOError(stripped_reply)

	def makeErrorGUI(self, title="Error!", message="An error has occured."):
		error_window = sg.Window(title).Layout([
								[sg.Text(message, auto_size_text=True, pad=(1,1))],
								[sg.OK(pad=(1,1))]
							])
		while(True):
			event, value = error_window.Read()
			if event == "OK" or event is None :
				break
