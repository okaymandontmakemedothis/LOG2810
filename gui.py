# from easygui import *
import settings
import usersettings
from PySimpleGUI import PySimpleGUI as sg
import os


class Gui:
	def __init__(self, title):
		self.title = title
		self.menu_message = settings.default_menu_msg
		self.layout = None
		self.window = None
		self.setLayoutMenu(self.menu_message)
		# self.return_value = None
		self.exit_status = False

		
	def setLayoutMenuDefault(self):
		self.layout = settings.default_layout_menu

	def setLayoutMenu(self, message, a=None):
		self.layout = 	[
							[sg.Text(message, size=(40,1))],
							[sg.Button(button_text=settings.choices[0], auto_size_button=True, pad=(1,1)), 
							sg.Button(button_text=settings.choices[1], auto_size_button=True, pad=(1,1)), 
							sg.Button(button_text=settings.choices[2], auto_size_button=True, pad=(1,1)), 
							sg.Button(button_text=settings.choices[3], auto_size_button=True, pad=(1,1))]

						]

	def setLayoutMap(self, message, ):

	# def getReturn(self):
	# 	return self.return_value

	# def setTitle(self, title):
	# 	if self.window is sg.Window: 
	# 		self.title = title
	# 		window.Refresh()#update window

	def makeGUI(self, graphImage=None):
		previous_reply =""

		while settings.reply!="(d) Quitter.":
			#fonction to update message with previous action at the top
			self.menu_message += settings.reply
			self.setLayoutMenu(self.menu_message)

			previous_reply = settings.reply
			#GUI call
			# settings.reply = buttonbox(message, title=title, image=graphImage, choices=settings.choices)

			window = sg.Window(self.title).Layout(self.layout)
			settings.reply, value = window.Read()

			#In case red button quit or cmd-q
			if(settings.reply is None):
				settings.reply = ""
				self.exit_status = True
				break

			#reset the message value
			self.menu_message = self.menu_message.replace(previous_reply, "")


	def makeReplyGUI(self, g):
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
					window = sg.Window(self.title, default_element_size=(30,1)).Layout(layout_bye)
					event, value = window.Read()
					if event == "Exit" or event is None :
						self.exit_status = True
						break

	def askFileNameGUI(self):
		reply=enterbox("Enter the name of the file : ")
		while 1:
			if reply=="" or reply == None:
				reply=enterbox("Enter the name of the file : ")
			else:
				stripped_reply = reply.replace(" ","").split('.')
				if len(stripped_reply)==2:
					if(stripped_reply[1]=='txt'):
						print(".txt is not needed")
						return stripped_reply[0]+'.'+stripped_reply[1]
				elif len(stripped_reply)==1:
					print(".txt has been added")
					return stripped_reply[0]+".txt"
				else: 
					raise IOError(stripped_reply)

	def makeErrorGUI(self, title="Error!", message="An error has occured."):
		error_window = Window(title).Layout([
								[sg.Text(message, auto_size_text=True, pad=(1,1))],
								[sg.OK(pad=(1,1))]
							])
		while(True):
			event, value = error_window.Read()
			if event == "OK" or event is None :
				break
