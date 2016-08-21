import collections
a = collections.Counter(input().strip())
b = collections.Counter(input().strip())
count = 0
for k in a:
	count += abs(a[k] - b[k]) if k in b else a[k]
	a[k] = b[k] = 0
for k in b:
	count += b[k]
print(count)