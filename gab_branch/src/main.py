from graphe import *

g = Graphe()


# Lecture du fichier ajout des nodes/edges au graphe
with open('centresLocaux.txt') as f:
	# firstSection: True si la ligne comporte les infos d'un node
	firstSection = True
	for x in list(f):
		if x == '\n':
			firstSection = False
		else:
			info = x.split(',')
			info = [int(i) for i in info]

			if firstSection:
				node = Node(info[0], info[1])
				g.addNode(node)
			else:
				edge = Edge(g.getNodes()[info[0]], g.getNodes()[info[1]], info[2])


g.printGraph()