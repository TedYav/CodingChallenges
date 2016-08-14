#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

p = 0
m = 0
for i in range(n):
	if arr[i] > 0:
		p = p + 1
	elif arr[i] < 0:
		m = m + 1
print(p/n)
print(m/n)
print((n-p-m)/n)
