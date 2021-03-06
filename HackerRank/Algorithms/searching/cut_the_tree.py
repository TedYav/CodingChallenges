import sys
import random

sys.setrecursionlimit(15000)
import time

"""
	CUT THE TREE:
		Objective: remove one edge from a tree such that the difference in sums of vertices between the two cuts
			Is as low as possible.

		OBSERVATION AFTER LAST ATTEMPT: recalculating subtree sums repeats a ton of work.

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

	def remove_neighbor(self, other):
		self.neighbors.remove(other)
		other.neighbors.remove(self)

	# thought: add nodes one by one and remove -- calculate closest sum to target
	# can start at any node
	def DFS_to_target(self, target):
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
