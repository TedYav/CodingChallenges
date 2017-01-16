import random
num = 2 * (10**5)
print(num)
s = ''
for i in range(num):
	s += str(random.randint(0,9))
print(s)