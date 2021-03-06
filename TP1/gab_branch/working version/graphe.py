
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
		self.distance = float("inf")
		self.visited = False
		self.previous = None

	def getId(self):
		return self.id

	def getRecharge(self):
		return self.recharge

	def getEdges(self):
		return self.edges

	def getDistance(self):
		return self.distance

	def setDistance(self, newDistance):
		self.distance = newDistance

	def getVisited(self):
		return self.visited

	def setVisited(self, arg):
		self.visited = arg

	def getPrevious(self):
		return self.previous

	def setPrevious(self, prev):
		self.previous = prev

	def addEdge(self, e):
		isPresent = False
		for x in self.edges:
			if e == x:
				isPresent = True
				break

		if not(isPresent):
			self.edges.append(e)


	#
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
		if ((self.node1.getId() == another_edge.getNode1().getId()) or (self.node1.getId() == another_edge.getNode2().getId())
		and ((self.node2.getId() == another_edge.getNode1().getId()) or (self.node2.getId() == another_edge.getNode2().getId()))):
			return self.getCost() == another_edge.getCost()
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

	def getNode(self, id):
		return self.nodes[id]

	def getRechargeStations(self):
		return self.rechargeStations

	def addNode(self, node):
		# Verify that the node Id is not already in the dict
		if not(node.getId() in self.nodes) :
			self.nodes[node.getId()] = node

	def addRechargeStation(self, node):
		if not(node.getId() in self.rechargeStations) :
			self.rechargeStations[node.getId()] = node

	def initialize(self):
		for x in self.nodes:
			self.nodes[x].setVisited(False)
			self.nodes[x].setDistance(float("inf"))
			self.nodes[x].setPrevious(None)
			if self.nodes[x].getRecharge() == 1:
				self.rechargeStations[self.nodes[x].getId()] = self.nodes[x]


	# Simple print of every nodes id's and their edges cost
	def printGraph(self):
		for x in self.nodes:
			print("Noeud: ", x)
			self.nodes[x].printEdges()

class Payload:
	def __init__(self, start_index, end_index, typePatient=None, typeVoiture= None):
		self.start_index = start_index
		self.end_index = end_index
		self.typePatient = typePatient
		self.typeVoiture = typeVoiture

	def setStartIndex(self, start_index):
		self.start_index = start_index

	def setEndIndex(self, end_index):
		self.end_index = end_index

	def setTypePatient(self, typePatient):
		self.typePatient = typePatient

	def getStartIndex(self):
		return self.start_index

	def getEndIndex(self):
		return self.end_index

	def getTypePatient(self):
		return self.typePatient

	def getTypeVoiture(self):
		return self.typeVoiture
