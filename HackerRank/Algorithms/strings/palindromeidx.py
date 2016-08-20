def isPalindrome(s):
	for i in range(len(s)):
		if(s[i] != s[len(s)-i-1]):
			return False
	return True;

t = int(input().strip())
for i in range(t):
	s = input().strip()
	idx = -1
	for j in range(len(s)):
		if(s[j] != s[len(s) - j - 1]):
			if(isPalindrome(s[j:len(s)-j-1])):
				idx = len(s) - j - 1
			elif(isPalindrome(s[j+1:len(s)-j])):
				idx = j
			break
	print(idx)