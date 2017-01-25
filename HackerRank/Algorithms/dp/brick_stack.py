def run():
	t = int(input().strip())
	for _ in range(t):
		height,width = map(int,input().strip().split())
		print(ways_to_build_wall(width, height))

def ways_to_build_wall(width, height):
	modulus = 10**9 + 7
	row_memo = calculate_rows(width, modulus)
	wall_memo = calculate_walls(width, height, row_memo, modulus)
	solid_wall_memo = calculate_solid_walls(width, wall_memo, modulus)
	return solid_wall_memo[width]

def calculate_rows(width, modulus):
	row_memo = [0 for i in range(width+1)]
	row_memo[0] = 1
	for i in range(1, width + 1):
		for j in range(1,5):
			if i-j >= 0:
				row_memo[i] += row_memo[i-j]
		row_memo[i] %= modulus
	return row_memo

def calculate_walls(width, height, row_memo, modulus):
	wall_memo = [0 for i in range(width+1)]
	wall_memo[0] = 1
	for i in range(1, width+1):
		wall_memo[i] = (row_memo[i] ** height)%modulus
	return wall_memo

# height doesn't matter at this point :)
def calculate_solid_walls(width, wall_memo, modulus):
	solid_wall_memo = [0 for i in range(width+1)]
	solid_wall_memo[1] = 1
	for i in range(2, width+1):
		invalid_walls = 0
		for j in range(1,i):
			invalid_walls += solid_wall_memo[j] * wall_memo[i-j]
			invalid_walls %= modulus
		solid_wall_memo[i] = (wall_memo[i] - invalid_walls) % modulus
	return solid_wall_memo

run()