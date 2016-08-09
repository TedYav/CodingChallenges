from functools import reduce
from collections import deque
from queue import PriorityQueue as q

class Node:
	children = []
	pred = None
	id = 0
	visited = False

	def addChild(self, node):
		if(not node in self.children):
			self.children.append(node)
			node.addChild(self)

	def __init__(self, id):
		self.id = id
		self.children = []
		self.pred = None
		self.visited = False

	def __str__(self):
		return "ID: {0}, VISITED: {1}, PRED: {2}, CHILDREN {3}".format(self.id, self.visited, self.pred.id if self.pred else None, list(map((lambda x: x.id),self.children) if self.children else []))

class MemoizedPathTree:
	numNodes = 0
	edges = []
	spTrees = []

	def getPath(self, start, end):
		if(not self.spTrees[start]):
			print("MISS! GENERATING PATH TREE FOR %d" % start)
			self.generatePathTree(start)
		else:
			print("HIT! PATH ALREADY CALCULATED FOR %d" % start)
		path = []
		node = self.spTrees[start][end]
		path.append(node.id)
		while node.id != start:
			node = node.pred
			path.append(node.id)
		return path

	def generatePathTree(self, start):
		self.spTrees[start] = [Node(x) for x in range(0, self.numNodes + 1)]
		for e in edges:
			self.spTrees[start][e[0]].addChild(self.spTrees[start][e[1]])
		self.bfs(self.spTrees[start][start])

	def bfs(self, node):
		node.visited = True
		for n in node.children:
			if(not n.visited):
				n.pred = node
				self.bfs(n)

	def printPathTree(self, target):
		if(self.spTrees[target]):
			print("\n".join([str(x) for x in self.spTrees[target] if x.id!=0]), "\n")
		else:
			print("Path tree not generated yet for %d. GENERATING" % target)
			self.generatePathTree(target)
			self.printPathTree(target)


	def __init__(self, numNodes, edges):
		self.spTrees = [x for x in [None]*(numNodes+1)]
		self.numNodes = numNodes
		self.edges = edges
		for e in edges:
			print("EDGE: {}".format(e))


class Suit:
	startTime = 0
	speed = 0
	currentPos = 0
	path = []
	start = 0
	end = 0

	def __str__(self):
		return "START-TIME: %d SPEED: %d START: %d END: %d CURRENTPOS: %d PATH: %s" \
			% (self.startTime, self.speed, self.start, self.end, self.currentPos, str(self.path))

	def __init__(self, startTime, speed, start, end, pathTree):
		self.startTime = startTime
		self.speed = speed
		self.start = start
		self.end = end
		self.path = pathTree.getPath(start, end)
		self.currentPos = -1

def reset():
	for i in range(1, numNodes + 1):
		nodes[i].reset()

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

# read number of nodes and suits
# line = str(input()).split()
line = data.popleft()
numNodes = int(line[0])
numSuits = int(line[1])

edges = []

# load in edges
for i in range(1, numNodes):
	line = data.popleft()
	edges.append([int(line[0]),int(line[1])])

paths = MemoizedPathTree(numNodes, edges)

suits = []
for i in range(0, numSuits):
	line = data.popleft()
	suits.append(Suit(int(line[0]), int(line[1]), int(line[2]), int(line[3]), paths))
	print("SUIT %d: %s" % (i, suits[i]))