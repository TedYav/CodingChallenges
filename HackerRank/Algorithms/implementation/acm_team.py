n,m = map(int,input().strip().split())
people = []
max_topics = 0
max_count = 0

for _ in range(n):
	people.append(input().strip())
	partner1 = people[-1]
	for partner2 in people[:-1]:
		topics = sum([1 if partner1[i] == '1' or partner2[i] == '1' else 0 for i in range(m)])
		if topics > max_topics:
			max_topics = topics
			max_count = 1
		elif topics == max_topics:
			max_count += 1

print(max_topics)
print(max_count)
