class Node:
	def __init__(self, value):
		self.visited = False
		self.value = value
		self.neighbors = []

	def add_neighbor(self, node):
		self.neighbors.append(node)
		node.neighbors.append(self)

	def delete_neighbor(self, node):
		self.neighbors.remove(node)
		node.neighbors.remove(self)

	# debugging
	def __str__(self):
		return "NODE %d: %s" % (self.value, str(list(map(lambda c: c.value, self.neighbors))))
	def __repr__(self):
		return str(self)

def run():
	queries = int(input().strip())
	for _ in range(queries):
		[n,m] = list(map(int, input().split()))
		connections = []
		for i in range(m):
			connections.append(tuple(map(int, input().split())))
		friends = make_graph(connections, n)
		friend_groups = [group for group in make_friend_groups(friends) if len(group) > 1]
		total = sum([group_total(group) for group in friend_groups])
		print(total)

def make_graph(connections, n):
	# to allow connections to match indexing
	graph = [Node(i) for i in range(n+1)]
	for connection in connections:
		graph[connection[0]].add_neighbor(graph[connection[1]])
	return graph[1:]

def make_friend_groups(friends):
	friend_groups = []
	for friend in friends:
		if not friend.visited:
			friend_groups.append(DFS(friend, save=True))
	return friend_groups


# to calculate max total for each group:
	# reset group (visited = 0 for all nodes)
	# total = num_people_in_group * (num_people_in_group - 1)
	# run DFS to find cycles
	# as soon as cycle is found:
		# total += num_people_in_group * (num_people_in_group - 1)
			# reasoning: for n people, at most n-1 friendships
		# delete edge causing cycle
		# continue DFS until all cyclic edges are removed
			# do not need to start over and reset graph
			# reasoning: removing one back edge will not affect existence of other back edges
		# when node with 1 child is found, add to leaves list
			# when deleting an edge, if either node has one child now, add to leaves list
	# once all cycles are removed:
		# take first item from leaves list
		# delete it
		# update leaves list (look at neighbor)
		# num_friends in group -= 1
		# total += num_friends_in_group * (num_friends_in_group - 1)
		# when num_friends_in_group == 1: break
	# return total

def group_total(group):
	# reset group
	for node in group:
		node.visited = False
	num_friends = len(group)
	
	# to avoid accidentally adding a node twice
	# if this takes too long I will make this a list and check logic more carefully :)
	# DONT NEED JUST KIDDING
	# leaves = set()
	total = num_friends*(num_friends-1)

	# DFS TO REMOVE CYCLES
	stack = [group[0]]
	while stack:
		node = stack.pop()
		
		# could have been pushed to stack before it was visited
		# don't want to process twice :)
		if not node.visited:
			node.visited = True
			for neighbor in node.neighbors:
				# CYCLE -- update total and delete edge
				if neighbor.visited:
					node.delete_neighbor(neighbor)
					# I DO NOT THINK I NEED THIS LOGIC
					# lets see if it works without
					# idea: when neighbor finishes, this edge will be gone and it's neighbors count will be 1
					# if len(node.neighbors) == 1:
					# 	leaves.add(node)
					# elif len(neighbor.neighbors) == 1:
					# 	leaves.add(neighbor)
					total += num_friends*(num_friends-1)
				else:
					stack.append(neighbor)
			# if len(node.neighbors) == 1:
			# 	leaves.add(node)

	# remove leaves one by one
	# don't want to operate on last leaf or we'll get negative friends
	# update total for each one
	# this is shameful:
	# try using it just as a list later

	# once all cycles are removed:
		# take first item from leaves list
		# delete it
		# update leaves list (look at neighbor)
		# num_friends in group -= 1
		# total += num_friends_in_group * (num_friends_in_group - 1)
		# when num_friends_in_group == 1: break

	# THIS COULD ACTUALLY BE CALCULATED AUTOMATICALLY -- break cycles
	# then do sum(n*n-1 for n in range)
	# leaves = list(leaves)
	# while len(leaves) > 1:
	# 	node = leaves[0]
	# 	leaves.remove(node)
	# 	# DEBUGGING
	# 	assert len(node.neighbors) == 1

	# 	neighbor = node.neighbors[0]
	# 	node.remove_neighbor(neighbor)
	# 	if len(neighbor.neighbors) == 1:
	# 		leaves.append(neighbor)
	# 	num_friends -= 1
	# 	total += num_friends*(num_friends-1)

	return total

def DFS(node, save=False):
	if save:
		nodes = []
	stack = [node]
	while stack:
		node = stack.pop()
		node.visited = True
		if save:
			nodes.append(node)

		for neighbor in node.neighbors:
			if not neighbor.visited:
				stack.append(neighbor)
	if save:
		return nodes

run()

# procedure:
# for each query:
	# add all nodes to graph
	# split into groups, delete orphans
		# use DFS
		# add nodes to list that are discovered on a single call
	# calculate max total for each group
	# add totals together and print