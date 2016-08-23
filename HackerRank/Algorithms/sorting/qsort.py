def qsort(arr):
	if(len(arr) <= 1):
		return arr
	pivot = arr[0]
	l = []
	r = []
	for i in range(1, len(arr)):
		if(arr[i] < pivot):
			l.append(arr[i])
		else:
			r.append(arr[i])
	l = qsort(l)
	r = qsort(r)
	l.append(pivot)
	l.extend(r)
	print(" ".join(str(c) for c in l))
	return l

n = int(input().strip())
arr = [int(i) for i in input().strip().split(' ')]

arr = qsort(arr)