def test(arr,expected,tc_num):
	print("TC# %d" % tc_num)
	result = partition(arr)
	assert result == expected, "TC# %d\tGOT: %r EXPECTED: %r" % (tc_num,result,expected)
	print("PASS")

def test_partition():
	test([],[],1)
	test([1,2],[1,2],2)
	test([2,1],[1,2],3)
	test([3,2,1],[1,2,3],4)
	test([1,2,3],[1,2,3],5)
	test([3,1,2],[1,2,3],6)
	test([5,4,3,1,2,3],[2,1,3,3,5,4],7)

def swap(arr,i,j):
	arr[i],arr[j] = arr[j],arr[i]

def partition(arr):
	if arr is None or len(arr) <= 1: return arr
	else:
		pivot = arr[-1]
		left = 0
		right = len(arr) - 2
		
		while right > left:
			while arr[left] <= pivot and left < right: left += 1
			while arr[right] > pivot and right > left: right -= 1
			if left < right and arr[left] > pivot:
				swap(arr,left,right)
				left += 1
				right -= 1
		# in case we converge on value <= pivot in last step
		if arr[left] <= pivot: left += 1
		swap(arr,left,-1)

		return arr

test_partition()
