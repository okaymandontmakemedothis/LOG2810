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


# the logic of the algorithm
# param
def dijkstraAlgo(graph, start, end):
	pass