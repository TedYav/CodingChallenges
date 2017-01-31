import sys
import random

def number_not_in_array(arr):
	values = set(arr)
	for i in range(len(arr)+1): if i not in values return i

def number_not_in_array(arr):
	if len(arr) == sys.maxsize: return -1
	else:
		values = set(arr)
		test = 0
		while test in values: test = random.randint(0,sys.maxsize)
		return test