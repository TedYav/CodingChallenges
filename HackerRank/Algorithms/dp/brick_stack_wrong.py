modulus = 10**9 + 7

from functools import reduce

def factorial(n): return 1 if n<= 1 else reduce(lambda x,y:x*y,range(1,n+1))
def nCr(n,r): return factorial(n)//(factorial(n-r)*factorial(r))


def run():
	t = int(input().strip())
	memo = {
		'single_rows': {}
	}
	for _ in range(t):
		height, width = map(int,input().strip().split())
		print(ways_to_build_wall(width,height,memo))

# calculate ALL ways to arrange
# subtract ways to arrange of width 1 and width-1, 2 and width-2, etc :)
# the combinations within them do not matter because it doesn't matter how many gaps we have 
# -- only that we have one at this point

# height 1 is 0 ways if > 4 :)
def ways_to_build_wall(width,height,memo):
	if (width,height) not in memo['walls']:
		for i in range(1,width+1):
			subtotal = (ways_to_arrange_row(i,memo) ** height) % modulus
			for j in range(1,i):
				subtotal -= (memo['walls'][(j,height)] * memo['walls'][(i-j,height)])%modulus
			memo['walls'][(i,height)] = subtotal
	return memo['walls'][(width,height)]


def ways_to_arrange_row(width,memo):
	if width not in memo['single_rows']:
		ways = [[1 if i==0 else 0 for i in range(width+1)] for j in range(5)]
		blocks = list(range(1,5))
		for i in range(1,width+1):
			for block in blocks:
				# print(block)
				ways[block][i] += ways[block-1][i]
				if i >= block:
					ways[block][i] += ways[block][i-block]
		memo['single_rows'][width] = ways[4][width]
	return memo['single_rows'][width]

# run()