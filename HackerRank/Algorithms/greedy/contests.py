def run():
	n,k = map(int, input().split())
	important = []
	unimportant = []
	for _ in range(n):
		value, flag = map(int, input().split())
		if flag:
			important.append(value)
		else:
			unimportant.append(value)
	print(maximize_luck(important, unimportant, k))

def maximize_luck(important, unimportant, k):
	important.sort(key=lambda x: -x)
	return sum(important[:k] + unimportant) - sum(important[k:])

run()