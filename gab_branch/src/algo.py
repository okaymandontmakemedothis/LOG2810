from graphe import *



# data to be gathered in a set
# param:
#	node: the node itself from the graph
#	distance: distance value from its neighbour (set to -1 for infinity)
#	visited: true if the node has been visited
class dijkstraNode:
	def __init__(self, node, distance, visited):
		self.node = node
		self.distance = distance
		self.visited = visited


# find the shortest path
# param
def plusCourtChemin(graph, start, end, patientCategory):

	graph.initialize()





def dijkstraMin(graph, start, end):

	start.setDistance(0)

	toBeVisited = {}
	for x in graph.getNodes():
		toBeVisited[x] = graph.getNode(x)

	currentNode = start

	shortestDistance = None
	while toBeVisited:
		temp = findClosestNeighbour(currentNode)
		if temp is not None:
			currentNode = temp
			del toBeVisited[currentNode.getId()]

	return currentNode


def findClosestNeighbour(node):

	closestNeighbour = None

	for x in node.getEdges():
		neighbour = None
		if x.getNode1() == node:
			neighbour = x.getNode2()
		else:
			neighbour = x.getNode1()

		if not neighbour.getVisited():
			neighbour.setDistance(node.getDistance() + x.getCost())

			if closestNeighbour == None:
				closestNeighbour = neighbour
			elif closestNeighbour.getDistance() > neighbour.getDistance():
				closestNeighbour = neighbour

			closestNeighbour.setVisited(True)
			closestNeighbour.setPrevious(node)
	return closestNeighbour
