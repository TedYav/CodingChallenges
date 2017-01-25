t = int(input().strip())
for _ in range(t):
	b,w = map(int,input().strip().split())
	x,y,z = map(int,input().strip().split())
	black_cost = min(x, y+z)
	white_cost = min(y, x+z)
	print(black_cost * b + white_cost * w)