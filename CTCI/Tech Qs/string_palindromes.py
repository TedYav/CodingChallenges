def compare_counts(arr1, arr2):
	for i in range(len(arr1)):
		if arr2[i] - arr1[i] != 0:
			return False
	return True

a = raw_input("String a:").strip().lower()
print(a)
b = raw_input("String b:").strip().lower()
print(b)

c1 = [0 for i in range(26)]
c2 = [0 for i in range(26)]

count = 0
positions = []

for c in a:
	c1[ord(c) - ord('a')] += 1

for i in range(len(b) + 1):
	if compare_counts(c1,c2):
		count += 1
		positions.append(i)

	if i < len(b):
		if i >= len(a):
			c2[ord(b[i-len(a)]) - ord('a')] -= 1

		c2[ord(b[i]) - ord('a')] += 1

print(count)
print(positions)


