"""

	MEDIAN OF TWO SORTED ARRAYS:
	len(a) = m, len(b) = n

	We can divide each array into two parts, split at indices i and j respectively.

	IF a and b were one array, median would be the (m+n)//2'nd element, if the length was odd,
	or average of (m+n)//2 and (m+n)//2 - 1'th elements if m+n was even.

	Thus, we want to find i and j such that i + j == m+n//2 + 1 if m+n is odd, and i+j == (m + n)//2  if m+n is even
	WITH THE CONDITION THAT: a[i] > b[j-1] AND b[j] > a[i-1] (updated because we're choosing elements 0 to i-1 from a,
	0 to j-1 from b --> this will mean we've selected a total of i+j elements)

	EDGE CASE: a_m < b_0 or b_n < a_0 (no overlay) e.g. [1,2] [3,4]
	length is even so we want to find i,j such that i+j == (m+n)//2 == 2
	if we choose i == 2, j == 0, then no way to check a[i] and b[j-1]. 
	BUT, if i == len(a) and j == 0, we CAN check b[j] and a[i-1]:
		b[0] == 3
		a[i-1] == 2
		PASS. This is the correct division.

	We set target to our desired value for i + j
	i == len(a) // 2
	j = target - i
	perform binary search on i, updating j as necessary.

	If we make a the smaller array, this will run in O(min(log(m),log(n))) time.
	We initially set i and j to len(a)//2, len(b)//2, and our target to what i+j must equal.

	When we HAVE i and j. If length of arrays is odd, we return max of a[i-1], b[j-1]
	IF EVEN: return (max(a[i-1],b[j-1]) + min(a[i],b[j]))/2.0 -- of course screening for impossible values.

"""

# ASSUMING m + n is not going to overflow. Can make allowances otherwise to discuss later.
# STILL SOME BUGS WITH INDICES. Solve later. :(


"""

[1,6,7,10]
[2,3,4,5,8,9]

[True, False, True]
A [1, 6, 7, 10] B [2, 3, 4, 5, 8, 9] I 2 J 3)
I 2 J 3
[True, False]
A [1, 6, 7, 10] B [2, 3, 4, 5, 8, 9] I 0 J 5)
I 0 J 5
[True, True]
A [1, 6, 7, 10] B [2, 3, 4, 5, 8, 9] I -1 J 6)
A [1, 6, 7, 10] B [2, 3, 4, 5, 8, 9] I -1 J 6

"""
"""

	MEDIAN OF TWO SORTED ARRAYS:
	len(a) = m, len(b) = n

	We can divide each array into two parts, split at indices i and j respectively.

	IF a and b were one array, median would be the (m+n)//2'nd element, if the length was odd,
	or average of (m+n)//2 and (m+n)//2 - 1'th elements if m+n was even.

	Thus, we want to find i and j such that i + j == m+n//2 + 1 if m+n is odd, and i+j == (m + n)//2  if m+n is even
	WITH THE CONDITION THAT: a[i] > b[j-1] AND b[j] > a[i-1] (updated because we're choosing elements 0 to i-1 from a,
	0 to j-1 from b --> this will mean we've selected a total of i+j elements)

	EDGE CASE: a_m < b_0 or b_n < a_0 (no overlay) e.g. [1,2] [3,4]
	length is even so we want to find i,j such that i+j == (m+n)//2 == 2
	if we choose i == 2, j == 0, then no way to check a[i] and b[j-1]. 
	BUT, if i == len(a) and j == 0, we CAN check b[j] and a[i-1]:
		b[0] == 3
		a[i-1] == 2
		PASS. This is the correct division.

	We set target to our desired value for i + j
	i == len(a) // 2
	j = target - i
	perform binary search on i, updating j as necessary.

	If we make a the smaller array, this will run in O(min(log(m),log(n))) time.
	We initially set i and j to len(a)//2, len(b)//2, and our target to what i+j must equal.

	When we HAVE i and j. If length of arrays is odd, we return max of a[i-1], b[j-1]
	IF EVEN: return (max(a[i-1],b[j-1]) + min(a[i],b[j]))/2.0 -- of course screening for impossible values.

"""

# ASSUMING m + n is not going to overflow. Can make allowances otherwise to discuss later.

def max_left(a,b,i,j):
	vals = []
	print("A %r B %r I %r J %r" % (a,b,i,j))
	if i > 0 and i-1 < len(a):
		vals.append(a[i-1])
	if j > 0 and j-1 < len(b):
		vals.append(b[j-1])
	return max(vals)

def min_right(a,b,i,j):
	vals = []
	if i < len(a):
		vals.append(a[i])
	if j < len(b):
		vals.append(b[j])
	return min(vals)

# MAY HAVE TO USE <= instead of <
def found_median(a,b,i,j):
	conditions = [True]
	if i > 0 and i-1 < len(a) and j < len(b):
		conditions.append(a[i-1] <= b[j])
	if j > 0 and j-1 < len(b) and i < len(a):
		conditions.append(b[j-1] <= a[i])
	print(conditions)
	print("A %r B %r I %r J %r)" % (a,b,i,j))
	return all(conditions)

class Solution(object):
    def findMedianSortedArrays(self,a,b):
    	if not a and not b: return 0
    	else:
    		# swap lengths to ensure
    		if len(a) > len(b): a,b = b,a
    		m = len(a)
    		n = len(b)
    		
    		target = (m + n + 1)//2
    		low = 0
    		high = m
    		i = low + (high-low)//2
    		j = target - i
    		while not found_median(a,b,i,j):
    			# [1,2] [3,4] i = 1
    			# a[i-1] == 1 b[j] == 4
    			# found median when a[i] > b[j-1] and b[j] > a[i-1]
    			print("I %r J %r" % (i,j))
    			if j < len(b) and b[j] < a[i-1]: # too much a, too little b
    				high = i - 1
    			else:
    				# a[i] < b[j-1]: # too far in b, too little in a
    				low = i + 1
    			i = low + (high-low)//2
    			j = target - i
    		
    		if (m+n)%2 == 1:
    			return max_left(a,b,i,j)
    		else:
    			return (max_left(a,b,i,j) + min_right(a,b,i,j))/2.0
