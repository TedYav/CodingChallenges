def length_of_common_substring(s1,s2):
	substring_length = 0
	for i in range(min(len(s1), len(s2))):
		if s1[i] == s2[i]: substring_length += 1
		else: break
	return substring_length

s = input().strip()
t = input().strip()
k = int(input().strip())
if k>= len(s) + len(t):
	print("Yes")
else:
	substring_length = length_of_common_substring(s,t)
	ops_to_change = len(s) + len(t) - 2*substring_length
	if k >= ops_to_change and (k-ops_to_change) % 2 == 0: print("Yes")
	else: print("No")
