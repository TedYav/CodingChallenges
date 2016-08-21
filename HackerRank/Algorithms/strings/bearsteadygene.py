# define the problem
# really what we're being asked
# is to find the smallest possible substring
# that contains all the letters which are
# present beyond n/4

# STRATEGY: start with minimum length, iterate right and left positions
# until we find the minimum substring

def valid(diff):
	return len([k for k in diff if diff[k] > 0]) == 0

import collections
n = int(input().strip())
s = input().strip()
counts = collections.Counter(s)
goal = {k: counts[k] - n//4 for k in counts if counts[k] > n//4}
length = 0
if(len(goal) > 0):
	minlength = sum([goal[k] for k in goal])
	[i,j] = [0,minlength-1]
	length = n

	curr = collections.Counter(s[i:j+1])
	diff = {k: goal[k] - curr[k] for k in goal}

	while(i < n - minlength - 1 and j < n):
		while(not valid(diff) and j < n-1):
			j += 1
			if s[j] in diff:
				diff[s[j]] -= 1
		if((j - i) + 1 < length and valid(diff)):
			length = (j - i) + 1

		i += 1
		if(s[i-1] in diff):
			diff[s[i-1]] += 1
print(length)