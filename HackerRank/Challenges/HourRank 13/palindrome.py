def isPalindrome(s):
	if(not s[0] == s[len(s) - 1]):
		return False
	else:
		if(len(s) <= 2):
			return True
		else:
			return isPalindrome(s[1:len(s)-1])

q = int(input().strip())
for i in range(q):
	[n, k] = [int(a) for a in input().strip().split(' ')]
	s = input().strip()
	l = 1
	for j in range(len(s)):
		for k in range(len(s) - 1, j+1, -1):
			if(isPalindrome(s[j:k+1])):
				l = k - j if k - j > l else l
	print(l)
