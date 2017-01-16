def run():
	q = int(input().strip())
	for _ in range(q):
		x = int(input().strip())
		print(num_xors(x))

def num_xors(x):
	pow = 0
	num = 0
	while x > 0:
		if not x & 1:
			num += 2 ** pow
		x >>= 1
		pow += 1
	return num

run()