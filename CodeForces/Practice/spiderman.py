# Examples
# input
# 3
# 1 2 3
# output
# 2
# 1
# 1
# input
# 5
# 1 1 5 1 1
# output
# 2
# 2
# 2
# 2
# 2

import math

n = int(raw_input())
moves = str(raw_input()).split()

winningPlayer = 2
for i in range(0,n):
	move = int(moves[i])
	if not move%2:
		winningPlayer = (winningPlayer % 2) + 1 
	print(winningPlayer)