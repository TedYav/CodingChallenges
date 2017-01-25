# import timeit
def run():
	height,width = map(int,input().strip().split())
	grid = [[c for c in input().strip()] for row in range(height)]
	perimeter = max_perimeter(grid, width, height)
	print(perimeter if perimeter > 0 else "impossible")

def max_perimeter(grid, width, height):
	left, up = calculate_possible_distances(grid, width, height)
	perimeter = 0
	for row1 in range(height - 1):
		for row2 in range(row1 + 1, height):
			row_delta = row2 - row1
			if 2*(width-1) + 2*row_delta <= perimeter:
				continue
			possible_columns = []
			for column in range(width):
				if up[row2][column] >= row_delta:
					possible_columns.append(column)
			left_index = 0
			right_index = 0
			while right_index < len(possible_columns):
				left_column = possible_columns[left_index]
				right_column = possible_columns[right_index]
				column_delta = right_column - left_column
				current_perimeter = 2*column_delta + 2*row_delta
				if current_perimeter <= perimeter or column_delta == 0:
					right_index += 1
					continue
				else:
					if left[row1][right_column] >= column_delta and left[row2][right_column] >= column_delta:
						perimeter = current_perimeter
						right_index += 1
					else:
						left_index += 1
			
	return perimeter

def calculate_possible_distances(grid, width, height):
	left = [[0 for i in range(width)] for j in range(height)]
	up = [[0 for i in range(width)] for j in range(height)]
	for row in range(height):
		for column in range(width):
			if grid[row][column] != 'x':
				if row > 0 and grid[row-1][column] != 'x':
					up[row][column] = up[row-1][column] + 1
				if column > 0 and grid[row][column-1] != 'x':
					left[row][column] = left[row][column-1] + 1
	return (left,up)

run()