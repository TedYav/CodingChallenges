import collections

q = int(input().strip())

# TODO: make an actual BFS function not this bullshit you should know better and be ashamed
class Node:
	def addAdj(self, node):
		self.adj.append(node)
		node.adj.append(self)

	def __init__(self, id):
		self.id = id
		self.visited = False
		self.distance = -1
		self.adj = []
		self.depth = 0

bfsQueue = collections.deque()
def bfs(node):
	node.visited = True
	node.distance = 6 * node.depth
	for n in node.adj:
		if not n.visited:
			n.visited = True
			n.depth = node.depth + 1
			bfsQueue.append(n)
	if(len(bfsQueue) > 0):
		bfs(bfsQueue.popleft())

for i in range(q):
	[n,m] = [int(i) for i in input().strip().split(' ')]
	g = [Node(j+1) for j in range(n)]

	for j in range(m):
		[s,e] = [int(i) for i in input().strip().split(' ')]
		g[s-1].addAdj(g[e-1])

	s = int(input().strip())
	g[s-1].depth = 0
	bfs(g[s-1])
	out = ""
	for i in range(len(g)):
		if g[i].id != s:
			prefix = " " if len(out) > 0 else ""
			out = out + prefix + str(g[i].distance)
	print(out)