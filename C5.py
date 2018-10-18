from easygui import *

def makeGUI(graphImage=None):
	choices = ["(a) Mettre a jour la carte.","(b) Determiner le plus court chemin securitaire.","(c) Extraire un sous-graphe.","(d) Quitter."]
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

		#logic of program after specific replies

		if reply == "(a) Mettre a jour la carte." :
			#break so that in the main we can call makeGUI again from the graphImage newly produced graph
			break


		# if reply == "(b) Determiner le plus court chemin securitaire.":


		#reset the message value
		message = message.replace(previous_reply, "")




# enterbox