#!/bin/python3

import sys


n = int(input().strip())

for i in range(n):
	s = ""
	for j in range(n):
		s = s + " " if j < (n-(i+1)) else s + "#"
	print(s)