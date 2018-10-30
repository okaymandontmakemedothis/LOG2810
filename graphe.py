
# Represent a node in the graph
# param:
# 	id: number associated with the node
#	recharge: node has a recharge point (1) or not (0)
#	edges: list of the edges connected to the current node
class Node:
	def __init__(self, id, recharge):
		self.id = int(id)
		self.recharge = recharge
		self.edges = []

	def getId(self):
		return self.id

	def getRecharge(self):
		return self.recharge

	def getEdges(self):
		return self.edges

	def addEdge(self, e):
		isPresent = False
		for x in self.edges:
			if e == x:
				isPresent = True
				break

		if not(isPresent):
			self.edges.append(e)


	# Simple print of the number of edges connected
	def printEdges(self):
		#for x in self.edges:
			#print(x.getCost())
		print(len(self.edges))


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

	def __eq__(self, another_edge):
		if self.node1.getId() == another_edge.getNode1().getId():
			if self.node2.getId() == another_edge.getNode2().getId():
				return True
		if self.node1.getId() == another_edge.getNode2().getId():
			if self.node2.getId() == another_edge.getNode1().getId():
				return True
		else:
			return False

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
		self.rechargeStations = {}

	def getNodes(self):
		return self.nodes

	def addNode(self, node):
		# Verify that the node Id is not already in the dict
		if not(node.getId() in self.nodes) :
			self.nodes[node.getId()] = node

	def addRechargeStation(self, node):
		if not(node.getId() in self.rechargeStations) :
			self.rechargeStations[node.getId()] = node

	# Simple print of every nodes id's and their edges cost
	def printGraph(self):
		for x in self.rechargeStations:
			print("Noeud: ", x)
			#self.nodes[x].printEdges()
			print(str(x) + "\n")
