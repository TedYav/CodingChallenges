# washing machines problem
# solution description
# We will keep track of the total deficit or total surplus in laundry at any point
# If there is a DEFICIT, we must move this to previous machines to balance them
# If there is a SURPLUS, we must move this to later machines to balance them
# The largest value of either is equal to the minimum number of moves to balance the machines

# We track this in a single variable delta, which tracks surpluses and deficits
# We just add the difference of each machine and target when we arrive at it
# This avoids the issue whereby a machine passes clothes in both directions.
# If the machine must pass clothes in only one direction, then delta is non-negative when we reach this machine

# E.G. {0 9 0} we get deltas (in order): {-3 +3 0} max == 3
# E.G. {5 3} ==> {+1 0}
# {5 5 2 2 2 2} ==> {+2 +4 +3 +2 +1 0} max == 4 
# (this is not 2 as my earlier solution would suggest because machine 2 must move 2 of its own clothes to machines 3-7
# AND it must move 2 of machine 1's clothes as well.)

def minimum_moves_to_balance(clothes):
	if not clothes or sum(clothes)%len(clothes) != 0:
		return None
	else:
		delta = 0
		max_delta = 0
		target_value = sum(clothes)//len(clothes)
		for i in range(len(clothes)):
			delta += clothes[i] - target
			max_delta = max(abs(delta), max_delta)
		return max_delta