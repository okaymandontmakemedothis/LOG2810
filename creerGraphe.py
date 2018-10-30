import os
from pprint import pprint
from gui import *
from graphe import *
import usersettings
import settings

def lireGraphe():
	try:
		name = askFileName()
		return creerGraphe(name);
	except IOError as e:
		print(type(e.args[0]))
		if type(e.args[0]) is list:
			# errorMsg = ""
			# for i in e.args[0]:
				# errorMsg+=i
			msgbox("IOError - An unexpected filename was entered: {0}".format(e))
		else:
			msgbox("{0}".format(e))
		
		# if type(e.args[0])==type(int):
			# errorMsg = "IOError - An unexpected filename was entered: {0}".format(e)
			# print(errorMsg)
			# msgbox()
		# else:
			# print(e.args[0])
			
		# if type(e.args[0])!=type(int):

		# else:
		# 	msgbox("IOError - The filename cannot be found: ",e.args[1][0])

	
def creerGraphe(nomFichier):
	g = Graphe()
	# Lecture du fichier ajout des nodes/edges au graphe
	with open(os.path.expanduser(usersettings.absolute_path_to_working_directory+nomFichier), 'r') as f:
		# firstSection: True si la ligne comporte les infos d'un node
		firstSection = True
		for x in list(f):
			if x == '\n':
				firstSection = False #firstSection: first half of the .txt with info to create Nodes
			else:
				info = x.split(',')
				info = [int(i) for i in info] # info = [ x1, x2, x3, ...]

				if firstSection: #create all the nodes with the available info from the .txt and add them to the graph (no edges yet)
					node = Node(info[0], info[1])
					g.addNode(node)
					if info[1] == 1:
						g.addRechargeStation(node)
				else: #create the edges
					node1 = g.getNodes()[info[0]]
					node2 = g.getNodes()[info[1]]
					cost = info[2]
					edge = Edge(node1, node2, cost) #Edge(node1, node2, cost)
	return g#do we need to return?

def askFileName():
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
# enterbox
