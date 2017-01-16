import sys

def min_coins(target, denominations):
	if target < 0 or not denominations:
		return None
	nums = [0]
	coins = [[]]
	for i in range(1, target + 1):
		nums.append(sys.maxint)
		coins.append([])
		min_coin = None
		for coin in denominations:
			if coin <= i:
				if nums[i-coin] + 1 < nums[i]:
					nums[i] = nums[i-coin] + 1
					min_coin = coin
		if min_coin:
			coins[i] = coins[i-min_coin] + [min_coin]
	return (nums[target], coins[target])