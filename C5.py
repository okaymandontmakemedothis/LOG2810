from easygui import *
import settings



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
		reply = buttonbox(message, image=graphImage, choices=settings.choices)

		#set the return_value before any break
		settings.return_value = reply

		#logic of program after specific replies

		if reply == "(a) Mettre a jour la carte." :
			#break so that in the main we can call makeGUI again from the graphImage newly produced graph
			break


		# if reply == "(b) Determiner le plus court chemin securitaire.":


		#reset the message value
		message = message.replace(previous_reply, "")

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
