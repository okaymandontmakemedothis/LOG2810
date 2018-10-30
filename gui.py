from easygui import *
import settings



def makeGUI(graphImage=None):
	message = "Action precedente : "
	title = settings.program_name
	previous_reply =""
	while settings.reply!="(d) Quitter.":
		#fonction to update message with previous action at the top
		message += settings.reply
		previous_reply = settings.reply
		#GUI call
		settings.reply = buttonbox(message, title=title, image=graphImage, choices=settings.choices)

		#set the return_value before any break
		settings.return_value = settings.reply

		#reset the message value
		message = message.replace(previous_reply, "")

		#logic of program after specific replies

		if settings.reply == settings.choices[0] :
			#break so that in the main we can call makeGUI again from the graphImage newly produced graph
			# await 
			break
		elif settings.reply == settings.choices[1] :
			# await
			break
		elif settings.reply == settings.choices[2] :
			# await
			break
		elif settings.reply == settings.choices[3] :
			# await 
			break

		# if reply == "(b) Determiner le plus court chemin securitaire.":

