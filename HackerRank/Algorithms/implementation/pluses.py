[x, y] = [int(s) for s in input().strip().split(' ')]

grid = []

for i in range(x):
	grid.append(list(input().strip()))

maxDim = x if x > y else y
maxArea = 0

#container for pluses that have been found so we can grow them and shrink them
pluses = [[] for i in range(0,maxDim + 1)]

for i in range(maxDim, 0, -1):
	# go down middle - place pluses

	# add all possible smaller pluses going down in size

	# calculate max area

	# iterate