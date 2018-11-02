from graphe import *


class AmbulanceNINH:
	def __init__(self, typePatient):
		self.typePatient = typePatient

	def calculateConsumption(self, minutes):
		consomption = 0
		if self.typePatient == 1:
			consomption = (minutes/60) * 6
		elif self.typePatient == 2:
			consomption = (minutes/60) * 12
		else:
			consomption = (minutes/60) * 48

		return consomption

class AmbulanceLIion:
	def __init__(self, typePatient):
		self.typePatient = typePatient

	def calculateConsumption(self, minutes):
		consomption = 0
		if self.typePatient == 1:
			consomption = (minutes/60) * 5
		elif self.typePatient == 2:
			consomption = (minutes/60) * 10
		else:
			consomption = (minutes/60) * 30

		return consomption

class Path:
	def __init__(self, start, end):
		self.start = start
		self.end = end
		self.orderedPath = []
		self.orderPath()

	def getStart(self):
		return self.start

	def getEnd(self):
		return self.end

	def getOrderedPath(self):
		return self.orderedPath

	def orderPath(self):
		currentNode = self.getEnd()
		while currentNode:
			self.orderedPath.append(currentNode)
			currentNode = currentNode.getPrevious()

		self.orderedPath.reverse()

	def printPath(self):
		print("Chemin: ")
		for x in self.orderedPath:
			print("\tNoeud: ", x.getId())
		print("\tTemps requis: ", self.end.getDistance())



# find the shortest path
def plusCourtChemin(graph, start, end, typePatient):

	graph.initialize()

	dijkstraAlgo(graph, start, end, True)

	p = Path(start, end) # path from start to finish found with dijkstraAlgo
	ambulanceNINH = AmbulanceNINH(typePatient)
	ambulanceLIion = AmbulanceLIion(typePatient)
	print("PLUS COURT CHEMIN")
	print("Le sort du patient est: ")
	if ambulanceNINH.calculateConsumption(end.getDistance()) < 80:
		print("Ambulance: NI-NH")
		print("Niveau de batterie final: ", 100 - ambulanceNINH.calculateConsumption(end.getDistance()),"%\n")
		p.printPath()
	else:
		# verifier avec rechargeStations
		path = findShortestPathWithRecharge(ambulanceNINH)
		if path is not None:
			pass
		elif ambulanceLIion.calculateConsumption(end.getDistance()) < 80:
			print("Ambulance: LI-ion")
			print("Niveau de batterie final: ", 100 - ambulanceLIion.calculateConsumption(end.getDistance()), "%\n")
			p.printPath()
		else:
			path = findShortestPathWithRecharge(ambulanceLIion)
			if path is not None:
				pass
			else:
				print("u ded")

def extraireSousGraphe(graph, start):
	print("EXTRAIRE SOUS-GRAPHE")

	graph.initialize()


	# il faut donner un parametre end a dijkstraAlgo donc on prend le 1er voisin
	voisin = None
	if start.getEdges()[0].getNode1().getId() == start.getId():
		voisin = start.getEdges()[0].getNode2()
	else:
		voisin = start.getEdges()[0].getNode1()

	dijkstraAlgo(graph, start, voisin, True)

	ambulanceNINH = AmbulanceNINH(1)	# 1 patient a risque faible
	ambulanceLIion = AmbulanceLIion(1)
	lePlusLoin = None
	for x in graph.getNodes():
		if (lePlusLoin == None) or (graph.getNodes()[x].getDistance() > lePlusLoin.getDistance()):
			# TODO: ajouter calculs de consommation de batterie
			c = ambulanceLIion.calculateConsumption(graph.getNodes()[x].getDistance())

			if c < 80:
				if lePlusLoin == None:
					lePlusLoin = graph.getNodes()[x]
				elif lePlusLoin.getDistance() < graph.getNodes()[x].getDistance():
					lePlusLoin = graph.getNodes()[x]

	if lePlusLoin != None:
		cheminLePlusLong = Path(start, lePlusLoin)
		cheminLePlusLong.printPath()
	else:
		print("Il est impossible de se deplacer à un autre noeud!!!")




def findShortestPathWithRecharge(ambulance):

	return None



# Find the shortest path with the Dijkstra algo
# param:
#	graph: graph to be used
#	start, end: nodes from graph
def dijkstraAlgo(graph, start, end, isMin):

	if (start.getId() == end.getId()) and isMin:
		print("noeuds de départ et d'arrivé sont les mêmes")
		return start

	start.setDistance(0)

	toBeVisited = {}

	# add all nodes from graph to the list of nodes to be visited
	for x in graph.getNodes():
		toBeVisited[x] = graph.getNode(x)

	while len(toBeVisited) > 0:

		u = minimum_distance(toBeVisited)

		# print("Noeud courant: ", u.getId(), " Distance: ", u.getDistance())

		del toBeVisited[u.getId()]

		if u.getDistance() == float("inf"):
			break

		setNeighboursDistance(u, isMin)

	return end

# Looks for the node with the smallest distance from all the unvisited nodes
# param:
#	nodes: unvisited nodes left
def minimum_distance(nodes):
	minimum = None
	for node in nodes:
		if (minimum == None) or (nodes[node].getDistance() < minimum.getDistance()):
			minimum = nodes[node]

	return minimum


# Set the distance for the unvisited neighbours
# param:
#	node: node from which we check the neighbours
def setNeighboursDistance(node, isMin):
	for x in node.getEdges():
		# v: neighbour of node
		v = None
		# an edged is composed of 2 nodes with no particular order
		# so we need to make sure we are not using the node passed in parameters
		# as its own neighbour
		if x.getNode1().getId() == node.getId():
			v = x.getNode2()
		else:
			v = x.getNode1()
		# update v's shortest path
		dist = node.getDistance() + x.getCost()
		if isMin:
			if (dist < v.getDistance()):
				v.setDistance(dist)
				v.setPrevious(node)
		else:
			if (dist > v.getDistance()) or (v.getDistance() == float("inf")):
				v.setDistance(dist)
				v.setPrevious(node)

def lireGraphe(Nodes):
	print("LIRE GRAPHE")

	GrapheString = ""
	for node in Nodes:
		GrapheString += "("
		GrapheString += "Noeud"+ str(node) #objet1
		GrapheString += ","
		GrapheString += str(Nodes[node].getId()) #numero1
		GrapheString += ", ("
		for edge in Nodes[node].getEdges():
			v = None
			if edge.getNode1().getId() == Nodes[node].getId():
				#Nodes[node].getNode2() = neighbour
				v = edge.getNode2()
			else:
				v = edge.getNode1()
				#Nodes[node].getNode2() = neighbour
			GrapheString += "(ObjetVoisin" + str(v.getId()) + ", " #str(Nodes[node].getEdges[neighbour])
			GrapheString += str(edge.getCost())
			GrapheString += "), "
		GrapheString = GrapheString[:-2] + "))"
		GrapheString += "\n\n"
	print(GrapheString)
