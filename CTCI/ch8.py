def fib_memoized(n, memo=[0,1,1]):
	if n < 1:
		return 0
	elif n <= 2:
		return 1
	else:
		if len(memo) > n:
			return memo[n]
		else:
			memo.append(fib_memoized(n-1, memo) + fib_memoized(n-2, memo))
			return memo[n]

def fib_bottom_up(n):
	fib = [0,1,1]
	n = 0 if n<0 else n
	for i in range(2, n+1):
		fib.append(fib[i-1] + fib[i-2])
	return fib[n]

def fib_opt(n):
	if n <= 2:
		return 1 if n > 0 else 0
	else:
		a = b = 1
		for i in range(n):
			a, b = b, a+b
	return a+b

def num_ways_to_climb(steps):
	ways_to_climb = [0 for i in range(steps+1)]
	ways_to_climb[:4] = [0, 1, 2, 4]
	for i in range(4, steps + 1):
		ways_to_climb[i] = sum(ways_to_climb[i-3:i])
	return ways_to_climb[steps]

def num_ways_to_goal(grid):
	if not grid: return 0
	r,c = len(grid), len(grid[0])
	if not r or not c: return 0

	num_ways = [[0 for i in range(c)] for j in range(r)]
	num_ways[r-1][c-1] = 1

	for i in range(r-1, -1, -1):
		for j in range(c-1, -1, -1):
			if grid[i][j] == 1:
				if i < r-1:
					num_ways[i][j] += num_ways[i+1][j]
				if j < c-1:
					num_ways[i][j] += num_ways[i][j+1]

	return num_ways[0][0]

def power_set(s):
	if not s:
		return [[]]
	else:
		subset_powerset = power_set(s[1:])
		return subset_powerset + [t + [s[0]] for t in subset_powerset]

def mult_slow(a,b):
	if a == 0 or b==0:
		return 0
	elif a == 1 or b == 1:
		return a if b == 1 else b
	else:
		return b + mult_slow(a-1, b)

def mult_fast(a,b):
	(a,b) = (b,a) if a > b else (a,b)
	if a==0:
		return 0
	elif a == 1:
		return b
	else:
		return mult_fast(a>>1, b<<1) + (b if a - ((a>>1)<<1) else 0)

def test_mult_fast(a,b):
	result = mult_fast(a,b)
	print(result)
	print(a*b)
	assert result == a*b

def hanoi(n):
	towers = [[i for i in range(n, 0, -1)], [], []]
	print(towers)
	move_discs(n, towers[0], towers[2], towers[1])
	print(towers)

def move_discs(n, source, destination, buf):
	if n == 1:
		destination.append(source.pop())
	elif n > 1:
		move_discs(n-1, source, buf, destination)
		move_discs(1, source, destination, None)
		move_discs(n-1, buf, destination, source)

def perms_recursive(s):
	if not s:
		return []
	elif len(s) == 1:
		return [s]
	else:
		permutations = []
		for i in range(len(s)):
			permutations.extend(s[i] + perm for perm in perms_recursive(s[:i] + s[i+1:]))
		return permutations

def perms_iterative(s):
	if not s:
		return []
	else:
		permutations = []
		stack = [("",s)]
		while stack:
			(base,string) = stack.pop()
			if len(string) == 1:
				permutations.append(base + string)
			else:
				stack.extend([(base + string[i],string[:i] + string[i+1:]) for i in range(len(string))])
		return permutations

def perms_duplicates(s):
	if not s:
		return []
	else:
		permutations = []
		chars = {char:s.count(char) for char in set(s)}
		stack = [("", chars)]
		while stack:
			(prefix, chars) = stack.pop()
			for c in chars:
				print(c)
				print(chars[c])

def parentheses(n):
	if not n:
		return ['']
	elif n == 1:
		return ['()']
	else:
		subset = parentheses(n-1)
		return list(set(['()' + parenthese for parenthese in subset] + ['(' + parenthese + ')' for parenthese in subset] + [parenthese + '()' for parenthese in subset]))

# insert left or right on each iteration
def parentheses_better(n, left=0, right=0):
	if n==0 and right == left:
		return [""]
	elif n==0:
		result = ""
		for i in range(right, left):
			result += ")"
		return [result]
	else:
		result = []
		result.extend(["(" + combo for combo in parentheses_better(n-1, left + 1, right)])
		if right < left:
			result.extend([")" + combo for combo in parentheses_better(n, left, right+1)])
		return result

def parentheses_better_stack(n):
	if not n:
		return []
	else:
		stack = [(0, 0, n, "")]
		results = []
		while stack:
			current = stack.pop()
			left = current[0]
			right = current[1]
			n = current[2]
			prefix = current[3]
			if n > 0:
				stack.append((left+1, right, n-1, prefix + "("))
				if right < left:
					stack.append((left, right+1, n, prefix + ")"))
			else:
				if right < left:
					results.append(prefix + ')' * (left-right))
				else:
					results.append(prefix)
		return results


test_grid = [[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0]]

def paint_fill_iterative(color, grid, i, j):
	if grid and valid_coord(grid, i, j):
		original_color = grid[i][j]
		if original_color != color:
			stack = [(i, j)]
			while stack:
				(i, j) = stack.pop()
				if valid_coord(grid, i, j) and grid[i][j] == original_color:
					grid[i][j] = color
					stack.extend([(i+1,j),(i-1,j),(i,j+1),(i,j-1)])

def paint_fill_recursive(color, grid, i, j):
	if grid and valid_coord(grid, i, j):
		original_color = grid[i][j]
		if original_color != color:
			grid[i][j] = color
			for coord in [(i+1, j), (i-1,j), (i, j+1), (i, j-1)]:
				if valid_coord(grid, coord[0], coord[1]) and grid[coord[0]][coord[1]] == original_color:
					paint_fill_recursive(color, grid, coord[0], coord[1])

def valid_coord(grid, i, j):
	return all([min(i,j)>=0, i<len(grid), j<len(grid[0])])

# BROKEN -- double counts a lot :)
# def num_ways_n_cents(n, coins=[25,10,5,1]):
# 	if n>=0:
# 		num_ways = [1 if i in coins else 0 for i in range(n+1)]
# 		for i in range(1, n+1):
# 			print(list(zip(num_ways, range(n))))
# 			for coin in coins:
# 				if coin <= i:
# 					print('adding %d' % i)
# 					num_ways[i] += num_ways[i-coin]
# 		return num_ways[n]

def num_ways_n_cents(n, coins=[1,5,10,25]):
	if n<0: return 0
	num_ways = [[(0 if i>0 else 1) for j in range(len(coins))] for i in range(n+1)]
	for i in range(1,n+1):
		for j in range(len(coins)):
			if i - coins[j] >= 0:
				num_ways[i][j] += num_ways[i-coins[j]][j]
			if j > 0:
				num_ways[i][j] += num_ways[i][j-1]
	return num_ways[n][len(coins)-1]

def eight_queens():
	valid_positions = []
	stack = [[]]
	while stack:
		positions = stack.pop()
		if len(positions) == 8:
			valid_positions.append(positions)
		else:
			target_row = len(positions)
			for position in get_valid_positions_in_row(target_row, positions):
				stack.append(positions + [(target_row, position)])
	return valid_positions

def get_valid_positions_in_row(row, positions):
	valid = [i for i in range(8)]
	if positions: # could combine this with next line
		for queen in positions:
			distance = row - queen[0]
			targets = [queen[1] - distance, queen[1], queen[1] + distance]
			for target in targets:
				if target in valid:
					valid.remove(target)
	return valid

def print_eight_queens():
	positions = eight_queens()
	for position in positions:
		print_position(position)

def print_position(position):
	for row in position:
		text = (" " * row[1]) + "X" + (" " * (8-row[1]))
		print(text)
	print("\n++++++++++++++\n")

class Box:
	def __init__(self, dimensions):
		self.width = dimensions[0]
		self.depth = dimensions[1]
		self.height = dimensions[2]

	def __lt__(self, other):
		return self.height < other.height

	def can_stack_under(self, other):
		return all([\
			self.height > other.height,\
			self.width > other.width,\
			self.depth > other.depth])

	def __str__(self):
		return 'BOX:\n h: %d\tw: %d\td: %d\n' % (self.height, self.width, self.depth)
	def __repr__(self):
		return str(self)

def maximum_stacking_height(boxes):
	if not boxes:
		return 0
	else:	
		boxes = sorted(list(map(Box, boxes)))[::-1]
		max_height = 0
		max_heights = [box.height for box in boxes]
		for i in range(len(boxes)-2, -1, -1):
			best = 0
			for j in range(i+1, len(boxes)):
				if boxes[i].can_stack_under(boxes[j]) and max_heights[j] > best:
					best = max_heights[j]
			max_heights[i] += best
			if max_heights[i] > max_height:
				max_height = max_heights[i]
		return max_height

print(maximum_stacking_height([[1,2,3],[4,5,6],[3,4,2],[1,3,3],[1,1,1]]))
