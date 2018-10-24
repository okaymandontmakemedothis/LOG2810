

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

	def printEdges(self):
		for x in self.edges:
			print(x.getCost())
		


class Edge:
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


class Graphe(object):
	def __init__(self):
		self.nodes = {}

	def getNodes(self):
		return self.nodes

	def addNode(self, node):
		self.nodes[node.getId()] = node

	def printGraph(self):
		for x in self.nodes:
			print("Noeud: ", x)
			self.nodes[x].printEdges()


