t = int(input().strip())
for _ in range(t):
	n = int(input().strip())
	print(len(list(filter(lambda digit: n%digit == 0, filter(lambda digit: digit != 0, [int(digit) for digit in str(n)] )))))