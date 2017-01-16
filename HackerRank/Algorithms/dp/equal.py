import sys

def run():
	t = int(input().strip())

	for _ in range(t):
		n = int(input().strip())
		people = list(map(int, input().split()))
		print(people)
		if not people:
			print(0)
		else:
			print(minimum_ops(people))

def minimum_ops(people):
	target = min(people)
	limit = max(people)
	costs = get_costs(limit-(target-5))

	min_ops = sys.maxsize
	for t in range(target, target-5, -1):
		ops = 0
		for p in people:
			ops += costs[p - t]
		min_ops = ops if ops < min_ops else min_ops
	return min_ops

_costs = None
def get_costs(cutoff):
	global _costs
	operations = [1, 2, 5]

	if not _costs:
		_costs = [sys.maxsize for i in range(cutoff + 1)]
		_costs[0] = 0
		start = 0
	elif len(_costs) < cutoff + 1:
		start = len(_costs)
		_costs.extend([sys.maxsize for i in range(cutoff + 1 - len(_costs))])
	else:
		start = cutoff + 1

	for i in range(start, cutoff+1):
		for operation in operations:
			if i - operation >= 0:
				_costs[i] = min(_costs[i], _costs[i-operation] + 1)

	return _costs

run()
