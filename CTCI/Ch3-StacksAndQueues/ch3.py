class Node:
	def __init__(self, value):
		self.v = value
		self.next = None

class Stack:
	def __init__(self):
		self._top = None

	def push(self, value):
		n = Node(value)
		n.next = self._top
		self._top = n

	def pop(self):
		if not self._top:
			raise Error("Empty Stack!")
		else:
			n = self._top
			self._top = self._top.next
			return n.v

	def peek(self):
		if not self._top:
			raise Error("Empty Stack!")
		else:
			return self._top.v

	def isEmpty(self):
		return True if self._top else False

	def __str__(self):
		n = self._top
		s = "TOP OF STACK: \n"
		while n:
			s += str(n.v) + "\n"
			n = n.next
		return s

	def __repr__(self):
		return self.__str__()

s = Stack()
print(s)
s.push(5)
print(s)
s.push(10)
s.push(20)
s.push(15)
print(s)
v = s.pop()
print("VALUE: %d" % (v))
print("___")
print(s)