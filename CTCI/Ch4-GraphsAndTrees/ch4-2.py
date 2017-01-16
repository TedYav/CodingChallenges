import random 

class RandBinTree:
	def __init__(self, root = None):
		self._root = root

	def insert(self, value):
		pass

	def delete(self, value):
		pass

	def random_node(self):
		if not self._root:
			return None
		else:
			node = self._root
			treesize = self._get_treesize(self._root)
			choice = random.randint(1,treesize)
			counts = []
			while sum(counts) != 1:
				counts = [self._get_treesize(node.left), 1, self._get_treesize(node.right)]
				if choice <= counts[0]:
					# DONT NEED TO SUBTRACT
					node = node.left
				elif choice == sum(counts[:2]):
					break
				else:
					choice -= sum(counts[:2])
					node = node.right
			return node

	def _get_treesize(self, node):
		if not node:
			return 0
		elif not node.treesize:
			if not (node.left or node.right):
				node.treesize = 1
			else:
				node.treesize = self._get_treesize(node.left) + 1 + self._get_treesize(node.right)
		return node.treesize

class Node:
	def __init__(self, value, parent = None):
		self.value = value
		self.left = None
		self.right = None
		self.treesize = None
		self.parent = parent

Btree = Node(10)
Btree.left = Node(5, Btree)
Btree.right = Node(12, Btree)
Btree.left.left = Node(2, Btree.left)
Btree.left.right = Node(10, Btree.left)
Btree.right.left = Node(11, Btree.right)
Btree.right.right = Node(15, Btree.right)

RBTree = RandBinTree(Btree)

for i in range(10):
	print(RBTree.random_node().value)