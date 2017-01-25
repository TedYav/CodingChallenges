def compare_grid(row_offset, col_offset, grid, pattern):

	for i in range(len(pattern)):
		for j in range(len(pattern[0])):
			if grid[i + row_offset][j + col_offset] != pattern[i][j]:
				return False
	return True

t = int(input().strip())
def scan_grid(rows): return [[int(i) for i in str(input().strip())] for j in range(rows)]
for _ in range(t):
	grid_rows, grid_cols = map(int,input().strip().split())
	grid = scan_grid(grid_rows)
	pattern_rows, pattern_cols = map(int, input().strip().split())
	pattern = scan_grid(pattern_rows)
	result = "NO"
	for i in range(grid_rows - pattern_rows + 1):
		for j in range(grid_cols - pattern_cols + 1):
			if compare_grid(i,j,grid,pattern):
				result = "YES"
				break
		if result == "YES":
			break
	print(result)