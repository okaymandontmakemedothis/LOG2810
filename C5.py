from easygui import *
import settings



def makeGUI(graphImage=None):
	message = "Action precedente : "
	title = ""
	previous_reply =""
	while settings.reply!="(d) Quitter.":
		#fonction to update message with previous action at the top
		message += settings.reply
		previous_reply = settings.reply
		#GUI call
		settings.reply = buttonbox(message, image=graphImage, choices=settings.choices)

		#set the return_value before any break
		settings.return_value = settings.reply

		#reset the message value
		message = message.replace(previous_reply, "")

		#logic of program after specific replies

		if settings.reply == "(a) Mettre a jour la carte." :
			#break so that in the main we can call makeGUI again from the graphImage newly produced graph
			break


		# if reply == "(b) Determiner le plus court chemin securitaire.":



#VERY HARD CODED... I don't at which point does it have to not be hard coded
def askFileName():
	reply=enterbox("Enter the name of the file : ")
	while 1:
		if reply=="" or reply == None:
			reply=enterbox("Enter the name of the file : ")
		else:
			stripped_reply = reply.strip()
			if stripped_reply ==reply+".txt":
				print(".txt is not needed")
				return stripped_reply
			elif stripped_reply == reply:
				print(".txt has been added")
				return stripped_reply+".txt"
# enterbox
