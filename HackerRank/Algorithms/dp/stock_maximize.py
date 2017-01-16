answers = [
46239752,
1975349587,
1121148693,
294370439,
913953487,
406783114,
151506355,
1430326358,
2182660642,
2163790409
]

def run():
	t = int(input().strip())
	for i in range(t):
		n = int(input().strip())
		prices = list(map(int, input().split()))

		# if i != 7:
			# continue
		profit = max_profit_n(prices,n)
		if profit != answers[i]:
			print("MISMATCH! DEBUG OUTPUT: ")
			print("MY ALGORITHM:")
			max_profit_n(prices,n,True)
			print("WORKING ALGORITHM:")
			max_profit_efficient(prices,n,True)
			print("END DEBUG OUTPUT")
		print(profit)

# gives wrong answer for inexplicable reason on SOME test cases
def max_profit_n(prices, n, debug = False):
	sell_points = []
	max_prices = []
	current_sell_price = 0
	for i in range(n-1, 0, -1):
		if prices[i] > current_sell_price:
			sell_points.append(i)
			max_prices.append(prices[i])
			current_sell_price = prices[i]
	if sell_points:
		if debug:
			# d = prices.index(97125)
			# print(prices[d-5:d+5])
			print(max_prices)
		profit = 0
		stock_count = 1
		for i in range(1,len(prices)):
			profit += (prices[i] - prices[i-1])*stock_count
			if i in sell_points:
				sell_points.pop()
				stock_count = 0
			else:
				stock_count += 1
		return profit
	else:
		return 0

def max_profit_efficient(prices, n, debug = False):
	max_price = 0
	profit = 0
	sell_points = []
	for price in prices[::-1]:
		if price > max_price:
			max_price = price
			sell_points.append(max_price)
		profit += max_price - price
	if debug:
		# d = prices.index(97125)
		# print(prices[d-5:d+5])
		print(sell_points)
	return profit

run()

def max_profit_n3(prices, n):
	profits = [[0 for i in range(n)] for j in range(n)]
	for day in range(1,n):
		for stock_count in range(day+1):
			delta = (prices[day] - prices[day - 1]) * stock_count
			min_stocks_yesterday = stock_count - 1 if stock_count > 0 else 0
			profits[day][stock_count] = max(profits[day-1][min_stocks_yesterday:day]) + delta
	return max(profits[n-1])

def max_profit_n2(prices, n):
	profits = [[0 for i in range(n)] for j in range(n)]
	for day in range(1,n):
		delta = (prices[day] - prices[day - 1]) 
		for stock_count in range(day, -1, -1):
			possibilities = []
			if stock_count > 0:
				possibilities.append(profits[day-1][stock_count - 1] + delta*stock_count)
			if stock_count < day:
				possibilities.append(profits[day][stock_count + 1] - delta)	# one less stock
			profits[day][stock_count] = max(possibilities)
	return max(profits[n-1])
