from functools import reduce 

def sample_balls(balls, number):
	if number < 1:
		return []
	elif number == 1:
		return [tuple([i]) for i in balls]
	elif number == len(balls):
		return [balls]
	else:
		return [tuple([balls[i]]) + j for i in range(len(balls) - number + 1) for j in sample_balls(balls[i+1:], number-1)]

def generate_initial_expected_values(sample_space, expected_values):
	for sample in sample_space:
		ev = 0
		for i in range(len(sample)//2):
			if sample[i] == 1 or sample[-(i+1)] == 1:
				ev += 2
			if len(sample) % 2 == 1:
				if sample[len(sample)//2] == 1:
					ev += 1
		ev /= len(sample)
		expected_values[sample] = ev

def update_expected_values(sample_space, prev_expected_values, expected_values):
	for sample in sample_space:
		expected_sample_value(sample, expected_values, prev_expected_values)

def expected_sample_value(sample, expected_values, prev_expected_values):
	ev = 0
	for i in range(len(sample)//2):
		# print("ANALYZING SAMPLE position %d:" % i)
		# print(sample)
		# if max(expected_value(sample, i, prev_expected_values, 2), expected_value(sample, len(sample)-i-1, prev_expected_values, 2)) == expected_value(sample, len(sample)-i-1, prev_expected_values, 2):
		# 	print("RIGHT!")
		# 	print("RESULT: ")
		# 	print(sample[:len(sample)-i-1] + sample[len(sample)-i:])
		# else:
		# 	print("LEFT!")
		# 	print("RESULT: ")
		# 	print(sample[:i] + sample[i+1:])
		ev += max(expected_value(sample, i, prev_expected_values, 2), expected_value(sample, len(sample)-i-1, prev_expected_values, 2))
		# print(ev)
		if len(sample) % 2 == 1:
			ev += expected_value(sample, len(sample)//2, prev_expected_values, 1)
	expected_values[sample] = ev

def expected_value(sample, i, expected_values, ways_to_reach):
	# print(sample)
	# print(i)
	# print(expected_values)
	return (ways_to_reach/len(sample)) * (sample[i] + expected_values[sample[:i] + sample[i+1:]])

def run():
	n,k = list(map(int,input().strip().split()))
	balls = input().strip()
	balls = tuple([1 if ball == 'W' else 0 for ball in balls])

	calculate(n,k,balls)

def calculate(n,k,balls):
	expected_values = {}
	prev_expected_values = {}

	# EZ MONEY
	if k == n:
		print("%.10f" % sum(balls))
	else:
		for q in range(n-k+1, n+1):
			prev_expected_values = expected_values
			expected_values = {}
			sample_space = sample_balls(balls, q)
			# print(sample_space)
			if q == n-k+1:
				generate_initial_expected_values(sample_space, expected_values)
			else:
				update_expected_values(sample_space, prev_expected_values, expected_values)
		print([expected_values[i] for i in expected_values][0])

# def debug():
# 	calculate(4,2,(1,0,1,0))
# run()