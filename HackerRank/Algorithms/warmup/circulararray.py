i = input().strip().split(' ')
# n = i[0]
k = int(i[1])
q = int(i[2])
n = [int(i) for i in input().strip().split(' ')]
for i in range(q):
	index = (int(input().strip()) - k) % len(n)
	print(n[index])