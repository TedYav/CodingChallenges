fib = [int(s) for s in input().strip().split(' ')]
limit = fib[2]
fib.pop()

for i in range(2,limit):
	fib.append((fib[i-1]*fib[i-1]) + fib[i-2])

print(fib[limit-1])