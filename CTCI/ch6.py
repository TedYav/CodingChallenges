import random

def birth_distribution_sim(families, rounds):
	boys = 0
	girls = 0
	for round in range(rounds):
		families_having_kids = families - girls
		if families_having_kids < 0:
			break

		for family in range(families_having_kids):
			birth_gender = random.random()
			if birth_gender >= 0.5:
				girls += 1
			else:
				boys += 1

		print_round_stats(round, families_having_kids, boys, girls)

def print_round_stats(round, families_having_kids, boys, girls):
	boys = float(boys)
	girls = float(girls)
	print("ROUND %d:" % round)
	print("families having kids: %d" % families_having_kids)
	print("boys: %d\tgirls: %d\t" %(boys, girls))
	print("boys: %.5f%%\tgirls: %.5f%%\n" % (((boys/(boys + girls))*100.0), ((girls/(boys + girls))*100.0)) )

def print_birth_distribution_sim(families, rounds):
	print("SIMULATING BIRTH RATES FOR %d ROUNDS AND %d FAMILIES:" % (rounds, families))
	birth_distribution_sim(families, rounds)