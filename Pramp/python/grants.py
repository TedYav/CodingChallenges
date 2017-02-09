"""

	Given array of grants and budget a, reduce total cost of grants to new budget b by capping all grants at c dollars.

	Affect the minimum number of granst.

	Naive: try c == 1...c == max(grants). O(n^2)
	Better: sort grants (O(nlogn)), subtract from first, then second, then third etc, total. As soon as total >= target, done. Calculate c.

"""

def minimum_budget(grants,new_budget):
	old_budget = sum(grants)
	grants = sorted(grants,reverse=True)
	target = old_budget - new_budget
	if new_budget < 0: return None
	elif target <= 0: return max(grants)
	else:
		total = 0
		for i in range(len(grants)-1):
			total += (grants[i] - grants[i+1])*(i+1)
			if total > target:
				return grants[i+1] + (total - target)//(i+1)