n = int(input().strip())
for i in range(n):
	s = input().strip()
	chars = {c: 1 for c in set(s)}
	cost = 0
	for j in range(len(s)):
		cost += chars[s[j]]
		chars[s[j]] = 0
	print(cost)