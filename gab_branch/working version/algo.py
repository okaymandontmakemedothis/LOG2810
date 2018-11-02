from graphe import *

separateur = "============================================================="

class AmbulanceNINH:
	def __init__(self, typePatient):
		self.typePatient = typePatient
		self.energyLevel = 100

	def getEnergyLevel(self):
		return self.energyLevel

	def setEnergyLevel(self, e):
		self.energyLevel = e

	def calculateConsumption(self, minutes):
		consomption = 0
		if self.typePatient == "Patient a faible risque":
			consomption = (minutes/60) * 6
		elif self.typePatient == "Patient a moyen risque":
			consomption = (minutes/60) * 12
		else:
			consomption = (minutes/60) * 48

		return consomption

class AmbulanceLIion:
	def __init__(self, typePatient):
		self.typePatient = typePatient

	def getEnergyLevel(self):
		return self.energyLevel

	def setEnergyLevel(self, e):
		self.energyLevel = e

	def calculateConsumption(self, minutes):
		consomption = 0
		if self.typePatient == "Patient a faible risque":
			consomption = (minutes/60) * 5
		elif self.typePatient == "Patient a moyen risque":
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
		self.tempsTotal = end.getDistance()


	def getStart(self):
		return self.start

	def getEnd(self):
		return self.end

	def getOrderedPath(self):
		return self.orderedPath

	def getTempsTotal(self):
		return self.tempsTotal

	def setTempsTotal(self, t):
		self.tempsTotal = t

	def orderPath(self):
		currentNode = self.getEnd()
		while currentNode:
			self.orderedPath.append(currentNode)
			currentNode = currentNode.getPrevious()

		self.orderedPath.reverse()

	def combinePaths(self, p2):
		p2.getOrderedPath().pop(0)
		for x in p2.getOrderedPath():
			self.orderedPath.append(x)

	def printPath(self):
		print("Chemin: ")
		for x in self.orderedPath:
			print("\tNoeud: ", x.getId())
		print("\tTemps requis: ", self.tempsTotal)



# find the shortest path
def plusCourtChemin(graph, payload):

	start = graph.getNode(payload.getStartIndex())
	end = graph.getNode(payload.getEndIndex())
	typePatient = payload.getTypePatient()


	graph.initialize()

	return_value = dijkstraAlgo(graph, start, end, True)
	if return_value==start:
		return


	p = Path(start, end) # path from start to finish found with dijkstraAlgo
	ambulanceNINH = AmbulanceNINH(typePatient)
	ambulanceLIion = AmbulanceLIion(typePatient)
	print("PLUS COURT CHEMIN")
	print("Le sort du patient est: ")
	if ambulanceNINH.calculateConsumption(end.getDistance()) < 80:
		print("Ambulance: NI-NH")
		print("Niveau de batterie final: ", "{0:.2f}".format(100 - ambulanceNINH.calculateConsumption(end.getDistance())),"%\n")
		p.printPath()
	else:
		# verifier avec rechargeStations
		path = findShortestPathWithRecharge(graph, start, end, ambulanceNINH)
		if path is not None:
			print("Il a fallu s'arreter pour recharger la batterie.")
			print("Ambulance: NI-NH")
			print("Niveau de batterie final: ", "{0:.2f}".format(ambulanceNINH.getEnergyLevel()), "%\n")
			path.printPath()
		elif ambulanceLIion.calculateConsumption(end.getDistance()) < 80:
			print("Ambulance: LI-ion")
			print("Niveau de batterie final: ", "{0:.2f}".format(100 - ambulanceLIion.calculateConsumption(end.getDistance())), "%\n")
			p.printPath()
		else:
			path = findShortestPathWithRecharge(graph, start, end, ambulanceLIion)
			if path is not None:
				print("Il a fallu s'arreter pour recharger la batterie.")
				print("Ambulance: LI-ion")
				print("Niveau de batterie final: ", "{0:.2f}".format(ambulanceLIion.getEnergyLevel()), "%\n")
				path.printPath()
			else:
				print("Nous sommes dans l'impossibilité de fournir des services au patient, car le transport n'a pas la batterie nécessaire.")

def extraireSousGraphe(graph, payload):
	print("EXTRAIRE SOUS-GRAPHE")

	start = graph.getNode(payload.getStartIndex())

	graph.initialize()


	# il faut donner un parametre end a dijkstraAlgo donc on prend le 1er voisin
	voisin = None
	if start.getEdges()[0].getNode1().getId() == start.getId():
		voisin = start.getEdges()[0].getNode2()
	else:
		voisin = start.getEdges()[0].getNode1()

	dijkstraAlgo(graph, start, voisin, True)

	ambulance = None
	print(payload.getTypeVoiture())
	if payload.getTypeVoiture() == "NI-NH":
		ambulance = AmbulanceNINH("Patient a faible risque")	# 1 patient a risque faible
	else:
		ambulance = AmbulanceLIion("Patient a faible risque")
		
	print(type(ambulance))

	lePlusLoin = None
	for x in graph.getNodes():
		if (lePlusLoin == None) or (graph.getNodes()[x].getDistance() > lePlusLoin.getDistance()):
			c = ambulance.calculateConsumption(graph.getNodes()[x].getDistance())

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




def findShortestPathWithRecharge(graph, start, end, ambulance):

	station = None
	path1 = None
	path2 = None
	time_total = float("inf")


	for r in graph.getRechargeStations():
		graph.initialize()
		dijkstraAlgo(graph, start, graph.getNode(r), True)
		if ambulance.calculateConsumption(graph.getNode(r).getDistance()) < 80:
			time_temp = graph.getNode(r).getDistance()
			path1 = Path(start, graph.getNode(r))
			graph.initialize()
			dijkstraAlgo(graph, graph.getNode(r), end, True)
			if ambulance.calculateConsumption(end.getDistance()) < 80:
				time_temp += end.getDistance()
				if time_temp < time_total:
					time_total = time_temp
					path2 = Path(graph.getNode(r), end)
					station = graph.getNode(r)
					ambulance.setEnergyLevel(100 - ambulance.calculateConsumption(end.getDistance()))

	if station == None:
		return None
	else:
		path1.combinePaths(path2)
		path1.setTempsTotal(time_total + 120)
		return path1



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
		# graph.getNode(x).setPrevious(graph.getNode(x))
		toBeVisited[x] = graph.getNode(x)

	while len(toBeVisited) > 0:

		u = minimum_distance(toBeVisited)

		# print("Noeud courant: ", u.getId(), " Distance: ", u.getDistance())

		del toBeVisited[u.getId()]

		# if u.getDistance() == float("inf"):
		# 	break

		setNeighboursDistance(u, isMin)

	#return end

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
