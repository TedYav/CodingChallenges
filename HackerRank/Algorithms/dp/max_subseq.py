def maximum_increasing_subsequence(array):
	if not array:
		return 0
	n = len(array)
	max_lengths = [1 for i in array]
	for i in range(n-1, -1, -1):
		for j in range(i+1, n):
			if array[j] > array[i] and max_lengths[j] >= max_lengths[i]:
				max_lengths[i] = max_lengths[j] + 1
	return max(max_lengths)

a = [1,3,2,4,6]
print(maximum_increasing_subsequence(a))