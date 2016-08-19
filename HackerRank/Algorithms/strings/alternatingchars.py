t = int(input().strip())
for i in range(t):
	s = list(input().strip())
	count = 0
	for j in range(len(s)-1):
		if s[j]==s[j+1]:
			count += 1
	print(count)