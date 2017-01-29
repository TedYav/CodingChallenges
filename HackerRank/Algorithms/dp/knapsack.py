def run():
	t = int(input().strip())
	for _ in range(t):
		n,k = map(int, input().strip().split())
		A = [0]	# start index from 1
		A.extend(list(map(int, input().strip().split())))
		print(knapsack(A,k,n))

def knapsack(arr,k,n):
	best = [[0 for i in range(k+1)] for j in range(n + 1)]
	for i in range(1,n+1):
		for j in range(1,k+1):
			possibilities = []
			possibilities.append(best[i][j-1])
			possibilities.append(best[i-1][j])
			if j >= arr[i]:
				possibilities.append(best[i-1][j-arr[i]] + arr[i])
				possibilities.append(best[i][j-arr[i]] + arr[i])
			best[i][j] = max(possibilities)
	return best[n][k]

run()