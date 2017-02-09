def quad_combo(arr,target):
	pair_sums = calculate_pair_sums(arr)
	result = None
	for sum1 in pair_sums:
		sum2 = target - sum1
		if sum2 in pair_sums:
			unique_indices = find_four_uniques(pair_sums, sum1, sum2)
			if unique_indices:
				result = unique_indices
				break
	return result

def calculate_pair_sums(arr):
	pair_sums = {}
	for i in range(len(arr)-1):
		for j in range(i+1, len(arr)):
			pair_sum = arr[i] + arr[j]
			if pair_sum in pair_sums:
				pair_sums[pair_sum].append((i,j))
			else:
				pair_sums[pair_sum] = [(i,j)]
	return pair_sums

def find_four_uniques(pair_sums, sum1, sum2):
	for pair1 in pair_sums[sum1]:
		for pair2 in pair_sums[sum2]:
			if pair1[0] not in pair2 and pair1[1] not in pair2:
				return [pair1[0],pair1[1],pair2[0],pair2[1]]
	return None

"""
import timeit
import random
def test_time_complexity(n=1000):
	pairs = [(random.randint(0,n//10), random.randint(0,n//10)) for i in range(n)]
	print(pairs)
	def a():
		for i in range(len(pairs)-1):
			for j in range(i+1,len(pairs)):
				pair1 = pairs[i]
				pair2 = pairs[j]
				if pair1[0] != pair2[0] \
					and pair1[0] != pair2[1] \
					and pair1[1] != pair2[0] \
					and pair1[1] != pair2[1]:
						result = [pair1[0],pair1[1],pair2[0],pair2[1]]
						pass

	def b():
		for i in range(len(pairs)-1):
			for j in range(i+1,len(pairs)):
				pair1 = pairs[i]
				pair2 = pairs[j]
				result = set([pair1[0],pair1[1],pair2[0],pair2[1]])
				if(len(set(result))==4):
					result = [pair1[0],pair1[1],pair2[0],pair2[1]]
					pass

	# CONSISTENTLY THE FASTEST
	def c():
		for i in range(len(pairs)-1):
			for j in range(i+1,len(pairs)):
				pair1 = pairs[i]
				pair2 = pairs[j]
				if(pair1[0] not in pair2 and pair1[1] not in pair2):
					result = [pair1[0],pair1[1],pair2[0],pair2[1]]
					pass

	def d():
		for i in range(len(pairs)-1):
			for j in range(i+1,len(pairs)):
				pair1 = pairs[i]
				pair2 = pairs[j]
				if(any(e in pair2 for e in pair1)):
					result = [pair1[0],pair1[1],pair2[0],pair2[1]]
					pass

	def e():
		for i in range(len(pairs)-1):
			for j in range(i+1,len(pairs)):
				if(pairs[i][0] not in pairs[j] and pairs[i][1] not in pairs[j]):
					result = [pairs[i][0],pairs[i][1],pairs[j][0],pairs[j][1]]
					pass

	time1 = timeit.timeit(a,number=1)
	time2 = timeit.timeit(b,number=1)
	time3 = timeit.timeit(c,number=1)
	time4 = timeit.timeit(d,number=1)
	time5 = timeit.timeit(e,number=1)
	print(time1)
	print(time2)
	print(time3)
	print(time4)
	print(time5)


test_time_complexity()

"""