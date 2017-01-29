"""

	CUT THE TREE:
	n-vertex tree t
	each vertex u has index from 1 to n and data d_u

	Cutting any edge u<-->v in tree t results in two trees, t1 and t2

	sum(t) == sum(data values in t)

	d_u,v = abs(sum(t1) - sum(t2))

	min 3, up to 10^5 vertices

	Tree always rooted at vertex 1

	Find edge u,v s.t. d_u,v is minimum

	all d_u,v are positive

	output minimum d_u,v possible for tree t



	OBSERVATIONS:
	BRUTE FORCE: try all and scan the tree.
		Since this is a tree, we have n-1 edges to pick from
			and n operations
			Thus O(N^2)

	BETTER: what if we store sums for various subtrees O(n)
	Then we remove an edge such that d_u,v is minimum

		==> data values are on vertices, so removing an edge will not affect sums

	Thus, any edge we remove::d_uv will be abs(sum(t1) - (sum(t)-sum(t1)))
		===> d_u,v = abs(sum(t)/2) - sum(t1)

	we can calculate for any edge in O(n) time

	Can do recursively to store sums at each node. We don't have to output vertices, just d_u,v
	Store each subtree sum in a list, use binary search to find value closest to sum(t)/2, return

	Store all nodes in array -- can access by value

"""

import sys

class Node:
	def __init__(self, value):
		self.value = value
		self.children = []
		self.tree_sum = -1

	# def add_child(self, node):
		# self.children.append

def run():
	n = int(input().strip())
	values = list(map(int, input().strip().split()))
	print(values)
	nodes = [Node(values[i]) for i in range(n)]
	for i in range(n-1):
		v1, v2 = map(int, input().strip().split())
		print(v1, v2)
		nodes[v1-1].children.append(nodes[v2-1])
	print(find_minimum_sum(nodes[0]))

# could improve if I were to insert into sorted data structure rather than list
# however linear search takes O(n) time, not going to kill me :)
# actually, sorted inserting would take O(n log n), so this is better
def find_minimum_sum(root):
	sums = []
	target = calculate_tree_sum(root, sums)/2
	print(target)
	print(sums)
	min_sum = min(map(lambda s: abs(target - s), sums))
	return min_sum

# will figure out stack based implementation later
def calculate_tree_sum(node, sums):
	node.tree_sum = node.value
	print(node.value)
	for child in node.children:
		node.tree_sum += calculate_tree_sum(child, sums)
	sums.append(node.tree_sum)
	return node.tree_sum

run()