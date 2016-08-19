n = int(input().strip())
a = [int(x) for x in list(input().strip())]
count = 0
i = 1
while i<n-1:
	if a[i-1] == 0:
		if a[i] == 1:
			if a[i+1] == 0:
				count = count + 1
				i = i + 2
	i = i + 1
print(count)