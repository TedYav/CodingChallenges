class Node:
	def __init__(self, val):
		self.next = None
		self.val = val

a = Node(5)
b = Node(5)
c = Node(10)
d = Node(5)

a.next = b
c.next = b
d.next = a

print(b is a)
print(c is a)
print(b == a)
print(c == a)

print(a.next == c.next)
print(a.next == d.next)

s1 = set([d, d.next, d.next.next])
s2 = set([c, c.next])
print(b in s1)
print(b in s2)
print(b in s1.intersection(s2))
print(len(s1.intersection(s2)))