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
def fact(n):
	if(n<=1):
		return 1
	else:
		return n * fact(n-1)

# not super efficient, but ok for this
def nCr(n,r):
	if r == 0: return 1
	return fact(n)//(fact(r) * fact(n-r))


# container to avoid the root deletion issue
class bTree():
	def __init__(self):
		self.root = Node()

	def __str__(self):
		return str(self.root)

	def add(self, val):
		self.root.addVal(val)

	def remove(self, val):
		self.root = self.root.delVal(val)

# TODO:
# refactor this monstrosity
# make it simpler
# use counter rather than list to avoid popping issue
class Node:
	def __init__(self, val=None,  parent=None):
		self.parent = parent
		self.initVal(val)

	def __str__(self):
		s = "";
		if(self.left):
			s += str(self.left)
		s += ("".join(self.val)) if self.val else ""
		if(self.right):
			s += str(self.right)
		# if((self.left and self.left.val and self.left.val > self.val) or (self.right and self.right.val and self.right.val <= self.val)):
		# 				print("WTF: SELF.VAL: ", self.val, " LEFT.VAL", self.left.val, " RIGHT.VAL: ", self.right.val)
		return s

	# cuts down on duplicate code
	# ensures we have dummy child nodes
	# but only if we are not a dummy
	def initVal(self, val):
		self.val = [val] if val else None
		self.left = Node(None, self) if val else None 
		self.right = Node(None, self) if val else None
	
	def addVal(self, val):
		if(self.val):
			if(val == self.val[0]):
				self.val.append(val)
			elif(val < self.val[0]):
				self.left.addVal(val)
			else:
				self.right.addVal(val)
		else:
			self.initVal(val)

	def findMin(self, cmin=None):
		if(not cmin or cmin > self.val[0]):
			cmin = self.val[0]
		return cmin if not self.left.val else self.left.findMin(cmin)

	def delVal(self, val):
		if(self.val):
			# print("DELETING: ", val, " FROM ", self.val, self.left.val, self.right.val)
			if(val == self.val[0]):
				if(len(self.val) > 1):
					self.val.pop()
				elif(len(self.val) == 1):
					if(self.left.val or self.right.val):
						if(self.left.val and self.right.val):
							# print("TWO CHILDREN: ", self.left.val[0], self.right.val[0])
							m = self.right.findMin()
							# print("MIN: ", m)
							self.right.delVal(m)
							self.val = [m]
						elif(self.left.val):
							if(self.parent):
								if(self.parent.val[0] > self.val[0]):
									self.parent.left = self.left
								else:
									self.parent.right = self.left
								self.left.parent = self.parent
							else:								
								self.left.parent = None
								return self.left
						else:
							if(self.parent):
								# print("PARENT VAL", self.parent.val, "MY VAL", self.val)
								# t = self.parent
								# while(t):
								# 	# print(t.val, t.left, t.right)
								# 	t = t.parent
								if(self.parent.val[0] < self.val[0]):
									self.parent.right = self.right
								else:
									self.parent.left = self.right
								self.right.parent = self.parent
							else:
								self.right.parent = None
								return self.right
					else:
						# print("CLEARING ", self.val)
						self.initVal(None)

			elif(val < self.val[0]):
				self.left.delVal(val)

			else:
				self.right.delVal(val)

		# otherwise return true, regardless of whether we deleted anything
		# print("RETURNING ", self)
		return self

t = int(input().strip())
for z in range(t):
	s = list(input().strip())

	count = Counter()

	# iterate ofer string sizes
	test = bTree()
	idx = 0
	direction = 1
	for i in range(1,len(s)):
		# print("LENGTH: ", i)

		test.add(s[idx + (i*direction) - direction])
		count.update({str(test): 1})
		# print(test)


		for j in range(len(s)-i):
			idx = idx + direction
			test.remove(s[idx - direction])
			test.add(s[idx + (i*direction) - direction])
			# print("ADDING: ", s[idx + (i*direction) - direction], idx + (i*direction) - direction, " DELETING: ", s[idx-direction], idx-direction)
			count.update({str(test): 1})
			# print(str(test))
			#pvmupwjjjf
			# print("REMOVING: ", s[idx-direction])
			# print(idx + (i*direction) - direction)
			# print("TEST: ", str(test))
			# print("COUNT: ", str(count))
		direction *= -1
		idx = 0 if direction == 1 else len(s) - 1

	# print(count)
	ways = [nCr(count[e],2) for e in set(count.elements()) if count[e] > 1]
	# print(ways)
	num = sum(ways)
	print(num)