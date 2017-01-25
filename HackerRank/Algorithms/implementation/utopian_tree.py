from functools import reduce
t = int(input().strip())
for _ in range(t):
	n = int(input().strip())
	print(reduce(lambda h,i: h * 2 if i % 2 == 0 else h + 1, range(n), 1))