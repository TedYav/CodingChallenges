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

class x

class Node:
	def __init(self, val,  parent=None):
		self.parent = parent
		self.initVal(val)

	def __str__(self):
		s = "";
		if(self.left.val):
			s += str(self.left)
		s += self.val
		if(self.right.val):
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
			target.leftPivot()
		elif(target.right.val):
			target.rightPivot()
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
				elif(self.parent):
					self.initVal(None)
				else:
					# in case we deleted THE WHOLE TREE!
					return False

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
	s = input().strip()
	c = Counter(s)
	print(c)
	c['z'] = 5
	print(c)
	print(hs(c))
	count = Counter(hs(c))
	print(count)
	count.update([hs(c))
	print(count)