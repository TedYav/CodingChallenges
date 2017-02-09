"""

Louise and Richard play a game. They have a counter set to . Louise gets the first turn and the turns alternate thereafter. In the game, they perform the following operations.

If N is not a power of 2, reduce the counter by the largest power of 2 less than N.
If  is a power of 2, reduce the counter by half of N.
The resultant value is the new  which is again used for subsequent operations.

If N==1 at beginning, Richard wins because Louise can't move.

OBSERVATIONS:
	If N is not a power of 2, reduce the counter by the largest power of 2 less than N.
		RESULT:
			Clear the left-most 1 bit of N.
	If  is a power of 2, reduce the counter by half of N.
		RESULT:
			Shift N to the right.

	Once we're in case 2, we will remain in case 2.

	What we're really doing is counting the number of 1 bits in n, 
		and the number of shifts required to make the right-most 1 bit into a 1.

	Number of moves it takes to win: number of 1 bits in n - 1 + number of right shifts required for last 1.

	If the answer is even, Richard wins. If it's odd, Louise wins.

"""

def solve():
	t = int(input().strip())
	for _ in range(t):
		n = int(input().strip())
		print(winner(n))

def winner(n):
	moves_to_win = 0
	first_one_found = False
	shifts = 0
	while n > 0:
		if n&1:
			if first_one_found:
				moves_to_win += 1
			else:
				moves_to_win += shifts
				first_one_found = True
		n >>= 1
		shifts += 1
	return "Richard" if moves_to_win % 2 == 0 else "Louise"

solve()