import sys
import random

sys.setrecursionlimit(15000)
import time

"""
	CUT THE TREE:
		Objective: remove one edge from a tree such that the difference in sums of vertices between the two cuts
			Is as low as possible.

		OBSERVATION AFTER LAST ATTEMPT: this isn't necessarily a binary tree, nor is there a well defined
			parent child relationship.

		Best strategy: sum up whole tree. Then cut each edge one by one and calculate sum of smaller half.
			May not know which half is smaller so just see if one is a leaf, calculate it. If not, pick random number.
				50% of time, it'll be smaller half. Should be fast enough.

		Other possible optimizations:
			* During initial pass, store edges by depth. Will help to always choose smaller half.
			* Store depth of vertices. Then calculate sum of half with smaller depth.
"""

class Node:
	def __init__(self, value):
		self.value = value
		self.neighbors = []
		self.visited = False

	def add_neighbor(self, other):
		self.neighbors.append(other)
		other.neighbors.append(self)
		# self.depth
	def remove_neighbor(self, other):
		self.neighbors.remove(other)
		other.neighbors.remove(self)

	def is_leaf(self):
		return len(self.neighbors) == 0

	# stack implementation to avoid recursion depth exceeded error
	def subtree_sum2(self):
		if self.visited: return 0
		else:
			subtree_sum = self.value
			self.visited = True
			for neighbor in self.neighbors:
				subtree_sum += neighbor.subtree_sum()
			self.visited = False
			return subtree_sum

	def subtree_sum(self):
		subtree_sum = 0
		stack = [self]
		done = []
		while stack:
			node = stack.pop()
			node.visited = True
			subtree_sum += node.value
			for neighbor in node.neighbors:
				if not neighbor.visited: stack.append(neighbor)
			done.append(node)
		for node in done: node.visited = False
		return subtree_sum

# in reality, tree wrapper class would be nice here
# but I'm just going to use an array of nodes for simplicity. This is Hackerrank :)

def solve():
	n = int(input().strip())
	values = list(map(int, input().strip().split()))
	nodes = [None] + [Node(values[i]) for i in range(n)] # 1 indexed
	edges = []
	for i in range(n-1):
		v1, v2 = map(int, input().strip().split())
		nodes[v1].add_neighbor(nodes[v2])
		edges.append((v1,v2))
	print(min_difference(nodes, edges))

# stop repeating so much work!
def min_difference(nodes, edges):
	min_diff = sys.maxsize
	total_sum = nodes[1].subtree_sum()
	# count = 0
	# start = time.time()
	for edge in edges[::-1]:
		# count += 1
		difference = get_difference_for_subtree(nodes, edge, total_sum)
		# print("COUNT: %d AVERAGE TIME: %.4f" % (count, (time.time() - start)/count))
		if difference < min_diff: min_diff = difference
		# print(min_diff)
	return min_diff

# recurisve: 0.01 seconds per edge
# stack: 0.008 seconds per edge

def get_difference_for_subtree(nodes, edge, total_sum):
	n1, n2 = nodes[edge[0]], nodes[edge[1]]
	n1.remove_neighbor(n2)
	if n1.is_leaf() or n2.is_leaf(): subtree_sum = n1.subtree_sum() if n1.is_leaf() else n2.subtree_sum()
	else: subtree_sum = n1.subtree_sum() if random.randint(0,1) == 0 else n2.subtree_sum()
	difference = abs(subtree_sum - (total_sum - subtree_sum))
	n1.add_neighbor(n2)
	return difference

solve()
