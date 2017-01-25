## DET SELECT -- strat 1
## BINARY SEARCH + PARTITION -- strategy 2

"""

	Find Max in array --> O(n)
	Find Min in array --> O(n)
	Since len(arr) is odd, goal is to find n s.t. n is in array, and partition(arr,n) creates two equal halves
	guess = (min + max)//2
	mid = partition(arr,n)
	while mid != len(array)//2:
		--> if value returned by partition is middle index of array
		--> then that is the median
		if mid is less than that, repartition the right using a new guess
		otherwise, repartition the left

"""

# Time: worst case O(nlogn)
import sys

def find_median(arr):
	low, high= min(arr), max(arr)
	guess = (low + high)//2
	start_index = 0
	stop_index = len(arr) - 1
	index = partition(arr, guess, start_index, stop_index)
	target = len(arr)//2
	while high >= low:
		# print("GUESS %d HIGH: %d LOW: %d STOP_INDEX: %d START_INDEX %d INDEX %d" % (guess, high, low, stop_index, start_index, index))
		if index > target:
			high = guess - 1
			stop_index = index
		else:
			low = guess + 1
			start_index = index
		guess = (low + high)//2
		index = partition(arr, guess, start_index, stop_index)
	return low

def swap(arr,i,j):
	arr[i],arr[j] = arr[j],arr[i]

def partition(arr, value, start=None, stop=None):
	if start is None or stop is None:
		start, stop = 0, len(arr) - 1
	# print("PARTITIONING AROUND %d "%value)
	left = start
	right = stop
	while right > left:
		while arr[left] <= value and left < stop: left += 1
		while arr[right] > value and right >= left: right -= 1
		if left < right:
			swap(arr,left,right)
			left += 1
			right -= 1
	# print("RESULT: %d" % left)
	return left


def find_median_2(array):
	return det_select(array, (len(array)//2) + len(array)%2)

def find_median_3(array):
	return detSelect(array, (len(array)//2) + len(array)%2)

# def detSelect(A, k, b=5):
#     #print("SEARCHING ", A, " FOR ", k, "th element.")
#     if(len(A) <= b):
#         A.sort()
#         return(A[k-1])
#     medians = list()
#     for i in range(len(A)//b):
#         temp = A[i*b:(i+1)*b]
#         temp.sort()
#         medians.append(temp[b//2])
#         #print("GROUP ", i, ": ", temp, " MEDIAN: ", temp[b//2])
#     #print("MEDIANS: ", medians)
#     mm = detSelect(medians, len(medians)//2, b)
#     #print("MM: ", mm)
#     left = list()
#     right = list()
#     for i in range(len(A)):
#         if A[i] <= mm:
#             left.append(A[i])
#         else:
#             right.append(A[i])

#     #print("LEFT ", left, " RIGHT ", right)

#     if k <= len(left):
#         return detSelect(left, k, b)
#     else:
#         return detSelect(right, k-len(left), b)

def det_select(array, k, divisions=5):
	if len(array) <= 5:
		array.sort()
		return array[k-1]
	else:
		medians = []
		n = len(array)
		for i in range((n//divisions) + (1 if n%divisions > 0 else 0)):
			temp = array[i*divisions:(i+1)*divisions]
			temp.sort()
			medians.append(temp[divisions//2] if len(temp)> divisions//2 else temp[-1])
		mm = det_select(medians, (len(medians)//2) + len(medians)%2)
		index = partition(array, mm) - 1
		if k <= index:
			return det_select(array[:index + 1],k)
		elif k > index:
			return det_select(array[index:],k-index)

import timeit

def run():
	n = int(input().strip())
	arr = list(map(int, input().strip().split()))
	print(find_median_2(arr))

import random
def timed_run(n=1000000):
	arr = [random.randint(-10, 10) for i in range(n)]
	# print(arr)
	time1 = 0
	time2 = 0
	for i in range(10):
		print("TEST %d:" % i)
		test = arr[:]
		def a(): find_median(test)
		time1 += timeit.timeit(a,number=1)
		# test = arr[:]
		# def b(): find_median_2(test)
		# time2 += timeit.timeit(b,number=1)
	print("TIME 1 (binary search + partition): %.5f, TIME 2 (deterministic selection): %.5f" % (time1/10, time2/10))

timed_run()