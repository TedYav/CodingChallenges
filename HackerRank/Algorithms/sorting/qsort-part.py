import random

n = int(input().strip())
arr = [int(i) for i in input().strip().split(' ')]

# pivot = random.randint(0, n-1)
pivot = 0
arr[pivot], arr[n-1] = arr[n-1], arr[pivot]
l = 0
for i in range(n-1):
	if(arr[i] < arr[n-1]):
		arr[i], arr[l], l = arr[l], arr[i], l+1
arr[n-1], arr[l] = arr[l], arr[n-1]
print(" ".join([str(i) for i in arr]))