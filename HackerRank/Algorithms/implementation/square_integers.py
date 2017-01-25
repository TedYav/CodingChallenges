from math import ceil, floor, sqrt
t = int(input().strip())
for _ in range(t):
	a,b = map(int, input().strip().split())
	print(len(range(ceil(sqrt(a)), floor(sqrt(b)) + 1)))