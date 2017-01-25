# 5 people get ad first day
# on each day, half like it and pass it on to 3 friends
n = int(input().strip())
total,current = 0,5
for i in range(n):
	total += current//2
	current = (current//2)*3
print(total)