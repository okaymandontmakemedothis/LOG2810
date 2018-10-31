from graphe import *


# find the shortest path
def plusCourtChemin(graph, start, end, patientCategory):

	graph.initialize()




# Find the shortest path with the Dijkstra algo
# param:
#	graph: graph to be used
#	start, end: nodes from graph
def dijkstraAlgo(graph, start, end, isMin):

	if start.getId() == end.getId():
		print("noeuds de départ et d'arrivé sont les mêmes")
		return start

	start.setDistance(0)
	# start.setVisited(True)

	toBeVisited = {}

	# add all nodes from graph to the list of nodes to be visited
	for x in graph.getNodes():
		# graph.getNode(x).setPrevious(graph.getNode(x))
		toBeVisited[x] = graph.getNode(x)

	while len(toBeVisited) > 0:

		# u = None
		# if isMin:
		# 	u = minimum_distance(toBeVisited)
		# else:
		# 	u = maximum_distance(toBeVisited)

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

# Looks for the node with the largest distance from all the unvisited nodes
# param:
#	nodes: unvisited nodes left
def maximum_distance(nodes):
	maximum = None
	for node in nodes:
		if (maximum == None):
			maximum = nodes[node]
		elif nodes[node].getDistance() > maximum.getDistance():
			if nodes[node].getDistance() != float("inf"):
				maximum = nodes[node]

	return maximum

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
		# if v.getVisited() == False:
		dist = node.getDistance() + x.getCost()
		if isMin:
			if (dist < v.getDistance()):
				v.setDistance(dist)
				v.setPrevious(node)
		else:
			if (dist > v.getDistance()) or (v.getDistance() == float("inf")):
				v.setDistance(dist)
				v.setPrevious(node)
