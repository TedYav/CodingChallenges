def run():
	(n,c,m) = map(int, input().split())
	passengers = list(map(int, input().split()))
	print("Yes" if can_travel(c, m, passengers) else "No")

def can_travel(capacity, num_boats, passengers):
	max_capacity = capacity * num_boats
	return all(map(lambda p: p <= max_capacity, passengers))

run()