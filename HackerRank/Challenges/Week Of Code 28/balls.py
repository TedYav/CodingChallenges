from functools import reduce

def run():
	n,k = list(map(int,input().strip().split()))
	balls = input().strip()
	balls = convert_balls(balls)
	
	# EZ MONEY
	if k == n:
		print("%.10f" % sum(balls))
	else:
		print("%.10f" % calculate_expected_value({balls: 1.0},k,initial_white_balls=sum(balls)))

# refactor -- arrangements should be hash table of position -- probability
def calculate_expected_value(arrangements,k,initial_white_balls):
	while k>0:
		arrangements = get_next_arrangements(arrangements, k)
		print(arrangements)
		k -= 1
	return expected_value(arrangements, initial_white_balls)

# test this
def get_next_arrangements(arrangements, k):
	next_arrangements = {}
	position_scores = {}
	for arrangement in arrangements:
		probability = arrangements[arrangement]
		position = arrangement
		for j in range(len(position)//2 + (1 if (len(position) % 2 == 1) else 0)):
			add_arrangement(next_arrangements, position_scores, position, j, probability, k)
	return next_arrangements

# test this :)
def add_arrangement(next_arrangements, position_scores, position, move, probability, k):
	result = get_move_result(position, move, probability, position_scores, k)
	if result[0] in next_arrangements:
		next_arrangements[result[0]] += result[1]
	else:
		next_arrangements[result[0]] = result[1]

# test this AND FINISH THIS :)
def get_move_result(position, move, previous_prob, position_scores, k):
	if len(position) % 2 == 1 and move == len(position)//2:
		return (position[:move] + position[move+1:], (1.0/len(position))*previous_prob)
	else:
		# may cache these too for speed :)
		left = position[:move] + position[move+1:]
		right = position[:len(position)-move-1] + position[len(position)-move:]
		if k == 1:
			return (left, (2.0/len(position))*previous_prob) if position[move] == 1 else (right, (2.0/len(position))*previous_prob)
		else:
			if score_position(left, position_scores, k) + (previous_prob * position[move]) > score_position(right, position_scores, k) + (previous_prob * position[len(position)-move-1]):
				return (left, (2.0/len(position))*previous_prob)
			else:
				return (right, (2.0/len(position))*previous_prob)

def expected_value(balls, initial_white_balls):
	return initial_white_balls - reduce(lambda x,y: x+(sum(y[0])*y[1]), map(lambda item: (item[0],item[1]), balls.items()), 0)

def convert_balls(balls):
	return tuple([1 if ball == 'W' else 0 for ball in balls])

def score_position(position, position_scores, k=0):
	if position not in position_scores:
		score = 0
		for i in range(len(position)//2):
			if position[i] == 1 or position[len(position) - i - 1] == 1:
				score += 2
			if k > 1:
				for j in filter(lambda x: position[x] == 1, [i, len(position) - i - 1]):
					score += (1/len(position))*score_position(position[:j] + position[j+1:], position_scores)
		if len(position) % 2 == 1:
			if position[len(position)//2] == 1:
				score += 1
				if k > 1:
					score += (1/len(position))*score_position(position[:len(position)//2] + position[(len(position)//2) + 1:], position_scores)
		position_scores[position] = (score/len(position))
	return position_scores[position]

run()