from graphe import *
from algo import *
import sys

# Version iterative
def creerGraphe(nomFichier):
	g = Graphe()
	# Lecture du fichier ajout des nodes/edges au graphe
	with open(nomFichier) as f:
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
	return g

#myGraph = creerGraphe(sys.argv[1])
myGraph = creerGraphe("centresLocaux.txt")

myGraph.printGraph()

dijkstraMin(myGraph, myGraph.getNode(1), myGraph.getNode(2)).printEdges()
