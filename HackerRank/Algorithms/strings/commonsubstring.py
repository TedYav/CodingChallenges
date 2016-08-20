# shortest python code ever :)
# I would never actually code like this if you're reading my github!
for i in range(int(input().strip())):
	print("YES" if (len(set(list(input().strip())).intersection(set(list(input().strip())))) > 0) else "NO")