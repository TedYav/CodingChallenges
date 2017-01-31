"""

	SPIRAL PRINT:
		Given matrix M, print all items of M in clockwise spiral order.

	METHODS:
		Mutating: set item to -1. Change direction upon encountering -1. 
			Doesn't support negative. Can use None in python.

		Non-Mutating: Copy and do #1 (takes space.)
			BETTER: Keep bounds. Upperbound, Lowerbound, Rightbound, Leftbound. Update.
			Direction --> use deltas. Encapsulate in class. (better overall)

"""

def spiral_print_simpler(matrix):
	top = 0
	bottom = len(matrix) - 1
	left = 0
	right = len(matrix[0]) - 1
	output = []
	while top <= bottom and left <= right:
		for i in range(left,right + 1):output.append(matrix[top][i])
		top += 1

		for i in range(top,bottom + 1): output.append(matrix[i][right])
		right -= 1

		if top <= bottom:
			for i in range(right, left - 1, -1): output.append(matrix[bottom][i])
			bottom -= 1

		if left <= right:
			for i in range(bottom, top - 1, -1): output.append(matrix[i][left])
			left += 1
	
	print(" ".join(map(str, output)))

def spiral_print(matrix):
	delta_row = 0
	delta_column = 1
	i = j = 0
	left_bound = -1
	top_bound = -1
	right_bound = len(matrix[0])
	bottom_bound = len(matrix)
	output = []
	while True:
		output.append(matrix[i][j])
		i += delta_row
		j += delta_column
		if i in [top_bound,bottom_bound] or j in[left_bound,right_bound]:
			if i==top_bound: left_bound += 1
			elif i==bottom_bound: right_bound -= 1
			elif j==right_bound: top_bound += 1
			elif j==left_bound: bottom_bound -= 1
			i -= delta_row
			j -= delta_column
			delta_row, delta_column = turn_right(delta_row, delta_column)
			i += delta_row
			j += delta_column
			if i in [top_bound,bottom_bound] or j in[left_bound,right_bound]:
				break
	print(" ".join(map(str,output)))

def turn_right(delta_row, delta_column):
	# right
	if delta_column != 0: return (1,0) if delta_column == 1 else (-1, 0)
	else: return (0,-1) if delta_row == 1 else (0,1)

def test_spiral_print():
	matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
	spiral_print(matrix)
	spiral_print_simpler(matrix)

test_spiral_print()