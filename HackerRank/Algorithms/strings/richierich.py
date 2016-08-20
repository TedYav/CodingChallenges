[n,k] = [int(s) for s in input().strip().split(' ')]
s = [int(s) for s in list(input().strip())]
t = [0 for c in s]

spent = 0

# make it a palindrome
for i in range(len(s)//2):
	if(s[i] != s[n-(i+1)]):
		if(s[i] > s[n-(i+1)]):
			s[n-(i+1)] = s[i]
			t[n-(i+1)] = 1
		else:
			s[i] = s[n-(i+1)]
			t[i] = 1
		spent += 1

# check if we succeeded
if(spent <= k):

	# make it the best palindrome
	if(spent < k):
		for i in range(len(s)//2 + 1):
			cost = 2 - int(s[i] == 9 or t[i] == 1) - int(s[n-(i+1)]==9 or t[n-(i+1)] == 1) - int((n-(i+1) == i))
			cost = cost if cost >= 0 else 0
			if(cost <= (k - spent)):
				s[i] = 9
				s[n-(i+1)] = 9
				spent += cost
			if(spent == k):
				break
	print("".join([str(c) for c in s]))

else:
	print(-1)