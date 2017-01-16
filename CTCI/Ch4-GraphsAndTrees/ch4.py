# class GraphNode:
# 	def __init__(self, value):
# 		self.visited = False # BFS and DFS
# 		self.marked = False	 # BFS
# 		self.value = value
# 		self.children = []

# 	def addChild(self, node):
# 		self.children.append(node)

# 	def visit(self):
# 		self.visited = True

# 	def set(self, value):
# 		self.value = value

# 	def mark(self):
# 		self.marked = True

# 	def reset(self):
# 		self.visited = False
# 		self.marked = False

# 	def clearChildren(self):
# 		self.children = []

# class BinTreeNode(GraphNode):
# 	def __init__(self, value):
# 		super(self, value)

# 	def isFull(self):
# 		return len(self.children == 2)

# 	def addChild(self, node):
# 		if self.isFull():
# 			raise IndexError('Node is full')
# 		else:
# 			self.children.append(node)

# 	def left(self):
# 		return self.children[0]

# 	def right(self):
# 		return self.children[1]

# 	def swap(self, target):
# 		self.value, target.value = target.value, self.value

# class ListNode:
# 	def __init__(self, value):
# 		self.value = value
# 		self.next = None

# class Queue:
# 	def __init__(self):
# 		self._head = None
# 		self._tail = None

# 	def dequeue(self):
# 		if not self.isEmpty():
# 			result = self._head
# 			if self._head == self._tail:
# 				self._head = self._tail = None
# 			else:
# 				self._head = self._head.next
# 			return result.value
# 		else:
# 			return None

# 	def enqueue(self, value):
# 		if not self.isEmpty():
# 			self._tail.next = ListNode(value)
# 			self._tail = self._tail.next
# 		else:
# 			self._head = ListNode(value)
# 			self._tail = self._head

# 	def isEmpty(self):
# 		return not (self._head and self._tail)

# class OrderedQueue:
# 	def __init__(self, comparison=lambda x,y : x<y):
# 		self._comp = comparison
# 		self._root = None
# 		self._tail = None
# 		self._count = 0

# 	def insert(self, value):
# 		self._count += 1

# 		if not self.isEmpty():
# 			parent = self.__getTailParent()
# 			child = BinTreeNode(value)
# 			parent.addChild(child)
# 			self.__bubbleUp(child)
# 		else:
# 			self._root = BinTreeNode(value)

# 	def __getTailParent(self):
# 		# using binary to figure out path to node
# 		steps = 0
# 		rpath = self._count
# 		path = 0
# 		while rpath > 0:
# 			path <<= 1
# 			steps += 1
# 			path |= rpath & 0b1
# 			rpath >>= 1

# 		path >>= 1
# 		parent = self._root
# 		for i in range(1, steps - 1):
# 			if path & 0b1 == 0:
# 				parent = node.left()
# 			else:
# 				parent = node.right()
# 			path >>= 1

# 		return parent

# 	def isEmpty(self):
# 		return self._root


# def binSearch(arr, value, lower=None, upper=None):
# 	if not (lower or upper):
# 		lower = 0
# 		upper = len(arr) - 1

# 	if upper - lower <= 1:
# 		return lower if arr[upper] > value else upper
	
# 	guess = ((upper - lower) // 2) + lower
	
# 	if arr[guess] > value:
# 		upper = guess
# 	else:
# 		lower = guess
	
# 	return binSearch(arr, value, lower, upper)

def bin_search(arr, value, lower=None, upper=None):
	if None in [lower, upper]:
		lower, upper = 0, len(arr)

	if upper - lower <= 1:
		return lower

	else:
		guess = ((upper - lower)//2) + lower
		if arr[guess] <= value:
			lower = guess
		else:
			upper = guess
		
		return bin_search(arr, value, lower, upper)

def topcoder_bin_search(pred, lower, upper):
	while lower < upper:
		guess = ((upper - lower) // 2) + lower
		print("LOWER %d UPPER %d GUESS %d" % (lower,upper,guess))
		if pred(guess):
			upper = guess
		else:
			lower = guess + 1
	return lower

test = [0, 5, 23, 44, 68, 128, 250, 343, 600, 780, 1000]
# print(test[bin_search(test, -500)])

# print(test[topcoder_bin_search( lambda x: (x+2 > len(test)), 0, len(test)  )])
def is_increasing(arr):
	return all(map(lambda x: x > 0, map(lambda x,y : y-x, arr,arr[1:]+ [sys.maxint])))

class Node:
	def __init__(self, value, parent=None):
		self.value = value
		self.left = None
		self.right = None
		self.parent = parent

Btree = Node(10)
Btree.left = Node(5, Btree)
Btree.right = Node(12, Btree)
Btree.left.left = Node(2, Btree.left)
Btree.left.right = Node(10, Btree.left)
Btree.right.left = Node(11, Btree.right)
Btree.right.right = Node(15, Btree.right)

tree = Node(10)
tree.left = Node(5)
tree.left.left = Node(2)
tree.left.right = Node(11)
tree.right = Node(12)
tree.right.left = Node(11)
tree.right.right = Node(15)

UBtree = Node(10)
UBtree.left = Node(5)
UBtree.right = Node(12)
UBtree.left.left = Node(2)
UBtree.left.right = Node(10)
UBtree.right.left = Node(11)
UBtree.right.right = Node(15)


BadBtree = Node(10)
BadBtree.left = Node(5)
BadBtree.right = Node(10)
BadBtree.left.left = Node(2)
BadBtree.left.right = Node(10)
BadBtree.right.left = Node(11)
BadBtree.right.right = Node(15)

import sys

def valid_BST(node, _min = -sys.maxint, _max = sys.maxint):
	conditions = []
	if node:
		conditions.append(node.value > _min)
		conditions.append(node.value <= _max)
		conditions.append(valid_BST(node.left, _min, node.value))
		conditions.append(valid_BST(node.right, node.value, _max))
	return all(conditions)

print("valid_BST -- BTree: \t%s" % valid_BST(Btree))
print("valid_BST -- UBtree: \t%s" % valid_BST(UBtree))
print("valid_BST -- tree: \t%s" % valid_BST(tree))
print("valid_BST -- BadBtree: \t%s" % valid_BST(BadBtree))


def io_verify(node, prev = -sys.maxint):
	if node is not None:
		prev = io_verify(node.left, prev)
		if node.value >= prev:
			prev = node.value
		else:
			raise ValueError()
		prev = io_verify(node.right, prev)
	return prev

def valid_BST2(root):
	try:
		io_verify(root)
		return "True"
	except:
		return False
		

print("valid_BST2 -- BTree: \t%s" % valid_BST2(Btree))
print("valid_BST2 -- UBtree: \t%s" % valid_BST2(UBtree))
print("valid_BST2 -- tree: \t%s" % valid_BST2(tree))
print("valid_BST2 -- BadBtree: \t%s" % valid_BST2(tree))

def successor(node):
	if node:
		if node.right:
			node = node.right
			while node.left:
				node = node.left
		else:
			while node.parent and node.parent.left is not node:
				node = node.parent
			node = node.parent
	return node

print(Btree.value)
print(successor(Btree).value)
print(successor(Btree.right.left).value)
print(successor(Btree.right.right))

def weave(a,b):
	if not a or not b:
		return [a] if a else [b]
	else:
		return [[a[0]] + c for c in weave(a[1:],b)] + [[b[0]] + c for c in weave(a,b[1:])]

print(weave([1,2],[3,4]))
