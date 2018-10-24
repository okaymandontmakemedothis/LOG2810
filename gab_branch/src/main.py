from graphe import *

g = Graphe()


# Lecture du fichier ajout des nodes/edges au graphe
with open('centresLocaux.txt') as f:
	# firstSection: True si la ligne comporte les infos d'un node
	firstSection = True
	for x in list(f):
		if x == '\n':
			firstSection = False #firstSection: first half of the .txt with info to create Nodes
		else:
			info = x.split(',')
			info = [int(i) for i in info]

			if firstSection: #create all the nodes with the available info from the .txt and add them to the graph (no edges yet)
				node = Node(info[0], info[1])
				g.addNode(node)
			else: #create the edges
				#Edge(node1, node2, cost)
				edge = Edge(g.getNodes()[info[0]], g.getNodes()[info[1]], info[2])


g.printGraph()