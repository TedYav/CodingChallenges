import queue

class Node:
	def __init__(self, value):
		self.visited = False
		self.value = value
		self.neighbors = []

	def add_neighbor(self, node):
		self.neighbors.append(node)
		node.neighbors.append(self)

	# debugging
	def __str__(self):
		return "NODE %d: %s" % (self.value, str(list(map(lambda c: c.value, self.neighbors))))
	def __repr__(self):
		return str(self)

class FriendGroup:
	def __init__(self, nodes):
		self._nodes = nodes
		self.num_friends = len(nodes)
		self.connections = sum([len(node.neighbors) for node in nodes])//2
		self.cycles = self.connections - (self.num_friends - 1)
		assert self.cycles >= 0

	def total(self):
		if self.num_friends > 0:
			return self.num_friends * (self.num_friends - 1)
		else:
			return 0

	def get_and_clear_cycles(self):
		cycles = self.cycles
		self.connections -= self.cycles
		self.cycles = 0
		return cycles

	def total_and_clear(self):
		total = 0
		# POSSIBLE ERROR: ADD AFTER OR BEFORE DECREMENTING
		while self.connections > 0:
			total += self.total()
			self.num_friends -= 1
			self.connections -= 1
		return total

	def __lt__(self, other):
		return self.connections < other.connections

	# debugging
	def __str__(self):
		return "FRIEND GROUP:\nNODES: %s\nFRIENDS: %d\nCONNECTIONS: %d\nCYCLES: %d\n" % (str(self._nodes), self.num_friends, self.connections, self.cycles)

	def __repr__(self):
		return str(self)

# procedure:
# for each query:
	# add all nodes to graph
	# split into groups, delete orphans
		# use DFS
		# add nodes to list that are discovered on a single call
	# calculate max total for each group
	# add totals together and print

	# TOTALS ARE INTERDEPENDENT
	# remove all cycles (sum of total_friends for each group)
	# remove edges from smallest groups one by one -- min queue
	# probably a good idea to wrap friend_groups in class so that they're orderable
	# then total them up, remove friends from each, total repeatedly
def run():
	queries = int(input().strip())
	for _ in range(queries):
		[n,m] = list(map(int, input().split()))
		connections = []
		for i in range(m):
			connections.append(tuple(map(int, input().split())))
		friends = make_graph(connections, n)
		# print(friends)
		friend_groups = make_friend_groups(friends)
		total = calculate_total(friend_groups)
		# total = sum([group_total(group) for group in friend_groups])
		print(total)

def calculate_total(friend_groups):
	total = 0
	round_total = sum([group.total() for group in friend_groups])
	rounds_to_clear_cycles = sum([group.get_and_clear_cycles() for group in friend_groups])
	total += round_total * rounds_to_clear_cycles
	group_queue = queue.PriorityQueue()
	for group in friend_groups:
		group_queue.put((group.num_friends, group))
	# may optimize this, but more prone to bugs -- let's see if this works first
	# optimization: subtract current group total from round_total
	while not group_queue.empty():
		(num_friends, group) = group_queue.get()
		# print(num_friends)
		round_total -= group.total()
		rounds_to_clear = group.num_friends - 1
		total += group.total_and_clear() + (round_total * rounds_to_clear)
		# print(total)
	return total

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
			nodes = DFS(friend)
			if len(nodes) > 1:
				friend_groups.append(FriendGroup(nodes))
	return friend_groups

def DFS(node):
	nodes = []
	stack = [node]
	while stack:
		node = stack.pop()
		if not node.visited:
			node.visited = True
			nodes.append(node)

			for neighbor in node.neighbors:
				if not neighbor.visited:
					stack.append(neighbor)
	return nodes

run()