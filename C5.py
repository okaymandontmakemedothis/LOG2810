from easygui import *
import settings

choices = ["(a) Mettre a jour la carte.","(b) Determiner le plus court chemin securitaire.","(c) Extraire un sous-graphe.","(d) Quitter."]

def makeGUI(graphImage=None):
	reply="Opened program"
	message = "Action precedente : "
	title = ""
	previous_reply =""
	while reply!="(d) Quitter.":
		#fonction to update message with previous action at the top
		message += reply
		previous_reply = reply
		#GUI call
		reply = buttonbox(message, image=graphImage, choices=choices)

		#set the return_value before any break
		settings.return_value = reply

		#logic of program after specific replies

		if reply == "(a) Mettre a jour la carte." :
			#break so that in the main we can call makeGUI again from the graphImage newly produced graph
			break


		# if reply == "(b) Determiner le plus court chemin securitaire.":


		#reset the message value
		message = message.replace(previous_reply, "")


def askFileName():
	return enterbox("Enter the name of the file : ")
	



# enterbox