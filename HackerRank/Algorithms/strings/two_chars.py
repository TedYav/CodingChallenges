### EZ SOLUTION ### -- O(n^2) -- large constant

import operator

def get_longest_filtered_string(s,counts):
	longest = 0
	for i in range(len(counts)-1):
		for j in range(i+1,len(counts)):
			if abs(counts[i][1] - counts[j][1]) <= 1:
				filtered_string = list(filter(lambda c: c in [counts[i][0],counts[j][0]], s))
				if verify(filtered_string):
					if len(filtered_string) > longest:
						longest = len(filtered_string)
	return longest

def verify(s): return all([s[i] != s[i-1] for i in range(1,len(s))])
				
n = int(input().strip())
s = input().strip()

counts = {}
for c in s:
	if c in counts: counts[c] += 1
	else: counts[c] = 1

counts = sorted(counts.items(),reverse=True,key=operator.itemgetter(1))

longest = get_longest_filtered_string(s,counts)
print(longest)


### HARD SOLUTION: O(n) ###
"""
import operator

n = int(input().strip())
s = input().strip()

counts = {}
for c in s:
	if c in counts: counts[c] += 1
	else: counts[c] = 1

possible_pairs = {}
counts = sorted(list(counts.items()),reverse=True,key=operator.itemgetter(1))
for i in range(len(counts)-1):
	if counts[i][1] - counts[i+1][1] <= 1:
		first_letter = counts[i][0]
		second_letter = counts[i+1][0]
		if first_letter in possible_pairs:
			possible_pairs[first_letter].add(second_letter)
		else:
			possible_pairs[first_letter] = set([second_letter])
		if second_letter in possible_pairs:
			possible_pairs[second_letter].add(first_letter)
		else:
			possible_pairs[second_letter] = set([first_letter])

last_observed = {c:-1 for c in possible_pairs.keys()}

for i in range(len(s)):
	if 
print(counts)

"""