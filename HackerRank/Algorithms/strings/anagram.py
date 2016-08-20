t = int(input().strip())
for i in range(t):
	s = input().strip()
	if(len(s) % 2):
		print(-1)
		continue
	count = 0
	w1 = s[0:len(s)//2]
	w2 = s[len(s)//2:]
	ltrs = set(list(w2))
	for c in ltrs:
		c2 = w2.count(c)
		c1 = w1.count(c)
		count += (c2 - c1) * int(c2 > c1)
	print(count)