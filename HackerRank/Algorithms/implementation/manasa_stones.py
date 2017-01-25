t = int(input().strip())
for _ in range(t):
	n = int(input().strip())
	a = int(input().strip())
	b = int(input().strip())
	possibilities = sorted(list(set([max(a,b) * i + min(a,b) * (n-i-1) for i in range(n)])))
	print(' '.join(map(str,possibilities)))