# GOAL: count number of contiguous substrings that have the same character content
# STRATEGY: iterate through array from size 1 to n/2, adding all elements to counter
# and then hashing the resulting character counts
# RUNNING TIME: O(n^3) with some large constants for the hash tables
# OKAY because we're working with ~100 elements

# NOTE: binary tree may be better than dict
# Even tho binary tree is O(log(N)) amortized
# searching through 26 elements is a larger constant
# because n <= 100

from collections import Counter

# class x

class Node:
	def __init__(self, val,  parent=None):
		self.parent = parent
		self.initVal(val)

	def __str__(self):
		s = "";
		if(self.left):
			s += str(self.left)
		s += self.val if self.val else ""
		if(self.right):
			s += str(self.right)
		return s

	# cuts down on duplicate code
	# ensures we have dummy child nodes
	# but only if we are not a dummy
	def initVal(self, val):
		self.val = val
		self.left = Node(None, self) if val else None 
		self.right = Node(None, self) if val else None
	
	def addVal(self, val):
		if(self.val):
			if(val <= self.val):
				self.left.addVal(val)
			else:
				self.right.addVal(val)
		else:
			self.initVal(val)

	def pivot(self, target):
		self.val = target.val
		if(target.left.val):
			target.pivot(target.left)
		elif(target.right.val):
			target.pivot(target.right)
		else:
			target.initVal(None)

	def delVal(self, val):
		if(self.val):
			if(val == self.val):
				if(self.left.val or self.right.val):
					if(self.left.val):
						self.pivot(self.left)
					else:
						self.pivot(self.right)
				else:
					self.initVal(None)
					# in case we deleted THE WHOLE TREE!
					return True if self.parent else False

			elif(val < self.val):
				self.left.delVal(val)

			else:
				self.right.delVal(val)

		# otherwise return true, regardless of whether we deleted anything
		return True

# roll own class with binary tree to speed this up
# if it's too slow
def hs(count):
	return "".join(sorted(c.elements()))

t = int(input().strip())
for z in range(t):
	s = list(input().strip())
	print(s)
	test = Node(s[0])
	print(test)
	for i in range(1,len(s)):
		test.addVal(s[i])
		print(test)
	for i in range(len(s)-1,-1,-1):
		result = test.delVal(s[i])
		print(test)
		print(result)