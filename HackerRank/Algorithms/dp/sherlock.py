def run():
	t = int(input().strip())
	for _ in range(t):
		n = int(input().strip())
		b = list(map(int, input().split()))
		print(max_cost(b))

def max_cost(b):
	f = [0 for i in b]
	g = [0 for i in b]
	for i in range(len(b)-2, -1, -1):
		f[i] = max(f[i+1], g[i+1] + (b[i] - 1))
		g[i] = max(f[i+1] + (b[i+1] - 1), g[i+1])
	return max(g[0], f[0])

run()
