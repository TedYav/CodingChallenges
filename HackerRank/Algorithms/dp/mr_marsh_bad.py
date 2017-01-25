perim_table = {}

def run():
	m,n = map(int,input().strip().split())
	grid = [[1 if c=='x' else 0 for c in input().strip()] for i in range(m)]
	perim = max_perimeter((0,0),(m-1,n-1),grid)
	print(perim if perim > 0 else "impossible")

def max_perimeter(u,v,grid):
	print((u,v))
	global perim_table
	if (u,v) not in perim_table:
		if u[0] >= v[0] or u[1] >= v[1]:
			perim_table[(u,v)] = 0
		else:

			perim, next_points = perimeter_or_next_points(u,v,grid)
			if perim > 0:
				return perim
			else:
				next_u, next_v = next_points
				perims = [0]
				for point in next_u:
					perims.append(max_perimeter(point,v,grid))
				for point in next_v:
					perims.append(max_perimeter(u,point,grid))

				perim_table[(u,v)] = max(perims)
	return perim_table[(u,v)]
def perimeter_or_next_points(u,v,grid):
	next_points = [[None,None],[None,None]]
	collision = False
	width = v[1] - u[1]
	height = v[0] - u[0]
	perim = 2*(width) + 2*(height)
	# top row
	i = 0
	while i <= width:
		if grid[u[0]][u[1]+i] == 1:
			collision = True
			while grid[u[0]][u[1]+i] == 1 and i < width:
				i += 1
			next_points[0][0] = (u[0],u[1]+i)
			next_points[0][1] = (u[0]+1,u[1])
			break
		i += 1

	# left side
	i = 0
	while i <= height:
		if grid[u[0]+i][u[1]] == 1:
			collision = True
			while grid[u[0]+i][u[1]] == 1 and i < height:
				i += 1
			next_points[0][1] = (u[0]+i,u[1])
			if next_points[0][0] is None:
				next_points[0][0] = (u[0],u[1]+1)
			break
		i += 1

	# bottom row
	i = 0
	while i <= width:
		if grid[v[0]][v[1]-i] == 1:
			collision = True
			while grid[v[0]][v[1]-i] == 1 and i < width:
				i += 1
			next_points[1][0] = (v[0],v[1]-i)
			next_points[1][1] = (v[0]-1,v[1])
			break
		i += 1

	# right side
	i = 0
	while i <= height:
		if grid[v[0]-i][v[1]] == 1:
			collision = True
			while grid[v[0]-i][v[1]] == 1 and i < height:
				i += 1
			next_points[1][1] = (v[0]-i,v[1])
			if next_points[0][0] is None:
				next_points[0][0] = (v[0],v[1]-1)
			break
		i += 1

	next_points[0] = filter(lambda x: x is not None, next_points[0])
	next_points[1] = filter(lambda x: x is not None, next_points[1])
	if collision: perim = 0
	return (perim, next_points)

run()