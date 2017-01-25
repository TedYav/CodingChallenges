n = int(input().strip())
cavity_map = [[int(c) for c in input().strip()] for _ in range(n)]
for i in range(1,n-1):
	for j in range(1,n-1):
		adjacent = [cavity_map[i][k] for k in [j-1, j+1]] + [cavity_map[k][j] for k in [i-1,i+1]]
		if 'X' not in adjacent:
			if max(adjacent) < cavity_map[i][j]:
				cavity_map[i][j] = 'X'
print('\n'.join([''.join(map(str,cavity_map[i])) for i in range(n)]))