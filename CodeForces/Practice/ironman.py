# Examples
# input
# 6 4
# 2 5
# 6 5
# 3 6
# 4 6
# 4 1
# 27 6 1 3
# 9 5 1 6
# 27 4 3 4
# 11 29 2 6
# output
# 27.3
# input
# 6 4
# 3 1
# 4 5
# 6 4
# 6 1
# 2 6
# 16 4 4 5
# 13 20 6 2
# 3 16 4 5
# 28 5 3 5
# output
# -1

from functools import reduce
from collections import deque

class Node:
	children = {}
	pred = None
	id = 0

	def addNode(self, node):
		if(not node.id in self.children):
			self.children[node.id] = node
			node.addNode(self)

	def setPred(self, node):
		self.pred = node

	def __init__(self, id):
		self.id = id
		self.children = {}
		self.pred = None

	def __str__(self):
		return str(self.id) + ": " + \
		str(list(self.children.keys()))

class PathMatrix:
	matrix = []
	nodes = []

	def addJunction(self, start, stop):
		print("ADDING JUNCTION %d %d" % (start, stop))
		self.matrix[start-1][stop-1] = [self.nodes[stop-1]]
		self.matrix[stop-1][start-1] = [self.nodes[start-1]]
		self.nodes[stop-1].addNode(self.nodes[start-1])
		self.nodes[start-1].addNode(self.nodes[stop-1])

	def shortestPath(self, start, stop):
		path = self.matrix[start-1][stop-1]
		if(path):
			print("I HAVE A PATH")
			print(path)
			path.append(self.nodes[0])
			print(path)
		else:
			print("NOPE")

	# basic implementation of Floyd Warshall algo
	# assumes all paths of length 0 and 1 are in graph
	def calcPaths(self):


	def __init__(self, count):
		self.matrix = [x[:] for x in [[None]*count]*count]
		self.nodes = [Node(x) for x in range(1,count+1)]
		for i in range(0, count):
			self.matrix[i][i] = [self.nodes[i]]

	def __str__(self):
		return str(list(map(lambda n: str(n),graph.nodes)))


data = deque([[6,4], \
		[2,5], \
		[6,5], \
		[3,6], \
		[4,6], \
		[4,1], \
		[27,6,1,3], \
		[9,5,1,6], \
		[28,4,3,4], \
		[11,29,2,6]])

# line = str(input()).split()
line = data.popleft()
numNodes = int(line[0])
numSuits = int(line[1])


# memoize shortest paths
graph = PathMatrix(numNodes)
print(graph.matrix)
print(graph)

for i in range(1, numNodes):
	# line = str(input()).split()
	line = data.popleft()
	print(line)
	graph.addJunction(int(line[0]), int(line[1]))

print(graph)
graph.shortestPath(4,6)
graph.shortestPath(1,6)
