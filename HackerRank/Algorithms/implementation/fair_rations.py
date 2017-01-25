n = int(input().strip())
distribution = list(map(int, input().strip().split()))
count = 0
for i in range(len(distribution)):
	if distribution[i] % 2 == 1:
		if i < len(distribution) - 1:
			distribution[i] += 1
			distribution[i+1] += 1
			count += 2
		else:
			count = "NO"
print(count)