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



# find the shortest path
def plusCourtChemin(graph, payload):

	graph.initialize()

	dijkstraAlgo(graph, payload.start, payload.end, True)

	ambulanceNINH = AmbulanceNINH(payload.typePatient)
	print("Le sort du patient est: ")
	if ambulanceNINH.calculateConsumption(payload.end.getDistance()) < 80:
		print("Ya assez de jus, t safe")
	else:
		print("u ded")




# Find the shortest path with the Dijkstra algo
# param:
#	graph: graph to be used
#	start, end: nodes from graph
def dijkstraAlgo(graph, start, end, isMin):
	if start.getId() == end.getId():
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

		print("Noeud courant: ", u.getId(), " Distance: ", u.getDistance())

		del toBeVisited[u.getId()]

		# if u.getDistance() == float("inf"):
		# 	break

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
	GrapheString = "("
	for node in Nodes:
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
		GrapheString += "\n\n"
	return GrapheString
