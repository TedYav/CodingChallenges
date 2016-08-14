#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

x = 0
y = 0
for i in range(n):
	x += a[i][i]
	y += a[n-i-1][i]
print(abs(x-y))