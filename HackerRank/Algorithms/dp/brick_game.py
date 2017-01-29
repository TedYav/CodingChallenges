def solve():
	t = int(input().strip())
	for _ in range(t):
		n = int(input().strip())
		bricks = [0]
		bricks.extend(list(map(int, input().strip().split()))[::-1]) # 1 indexed REVERSED OOPS LOL
		print(maximum_score(bricks,n))

"""

	BRICKS GAME:
		On each turn, we remove 1, 2, or 3 bricks from top of stack:
			b_j, b_j-1, b_j-2 for stack of height j. I get sum of scores.

		My opponent will also play optimally. How can I maximize my score?
		I will go first.

	STRATEGY:
		let f(i,p) = maximum score I can earn starting with stack of height i, with player p moving first
			p == 0 :: I'm moving first
			p == 1 :: Opponent moving first
			
			if p == 0:
				f(i,p) = max([f(i-1,1-p) + b_i, f(i-2,1-p) + b_i + b_i-1, f(i-3,1-p) + b_i + b_i-1 + b_i-2 ])
			if p == 1:
				f(i,p) = min([f(i-1,1-p) + b_i, f(i-2,1-p) + b_i + b_i-1, f(i-3,1-p) + b_i + b_i-1 + b_i-2 ])
			f(i,p) = 0 for all i <= 0

		Return f(n,0)

"""

def maximum_score(bricks, n):
	scores = [[0,0] for i in range(n+1)] # 1 indexed
	for i in range(1,n+1):
		for p in range(2):
			possibilities = []
			if p == 0:
				possibilities.append(get_score(scores, i-1, 1-p) + get_bricks(bricks, [i]))
				possibilities.append(get_score(scores, i-2, 1-p) + get_bricks(bricks, [i,i-1]))
				possibilities.append(get_score(scores, i-3, 1-p) + get_bricks(bricks, [i,i-1,i-2]))
				scores[i][p] = max(possibilities)
			else:
				possibilities.append(get_score(scores, i-1, 1-p))
				possibilities.append(get_score(scores, i-2, 1-p))
				possibilities.append(get_score(scores, i-3, 1-p))
				scores[i][p] = min(possibilities)
	return scores[n][0]

def get_score(scores, i, p): return scores[i][p] if i >= 0 else 0

def get_bricks(bricks, indices): return sum([get_brick(bricks, i) for i in indices])
def get_brick(bricks, i): return bricks[i] if i >= 0 else 0

solve()