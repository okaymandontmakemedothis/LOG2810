
# Represent a node in the graph
# param:
# 	id: number associated with the node
#	recharge: node has a recharge point (1) or not (0)
#	edges: list of the edges connected to the current node
class Node:
	def __init__(self, id, recharge):
		self.id = id
		self.recharge = recharge
		self.edges = []

	def getId(self):
		return self.id

	def getRecharge(self):
		return self.recharge

	def getEdges(self):
		return self.edges

	def addEdge(self, e):
		self.edges.append(e)


	# Simple print of every edge's cost linked to the current node
	def printEdges(self):
		for x in self.edges:
			print(x.getCost())
		

# Represent an edge linking 2 nodes
# param:
#	node1, node2: nodes linked togheter
#	cost: cost associated to the edge
class Edge:
	
	# When built, an edge adds itself to the 2 nodes it links togheter
	def __init__(self, node1, node2, cost):
		self.node1 = node1
		self.node2 = node2
		self.cost = cost
		node1.addEdge(self)
		node2.addEdge(self)

	def getCost(self):
		return self.cost

	def getNode1(self):
		return self.node1

	def getNode2(self):
		return self.node2


# Represent the full graph
# param:
#	nodes: list of nodes currently in the graph
class Graphe(object):
	def __init__(self):
		self.nodes = {}

	def getNodes(self):
		return self.nodes

	def addNode(self, node):
		self.nodes[node.getId()] = node

	# Simple print of every nodes id's and their edges cost
	def printGraph(self):
		for x in self.nodes:
			print("Noeud: ", x)
			self.nodes[x].printEdges()


