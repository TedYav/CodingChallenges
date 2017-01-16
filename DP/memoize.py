def MemoizedFunction(f):
    mem = dict()
    def g(*args):
        if args not in mem:
            mem[args] = f(*args)
        return mem[args]
    return g

def fib(n):
	if n < 1:
		return 0
	elif n <= 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

mFib = MemoizedFunction(fib)
print(fib(10))
print(fib(30))
print(mFib(10))
print(mFib(50))