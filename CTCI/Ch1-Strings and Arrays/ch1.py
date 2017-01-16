def isPalindromePermutation(s):
	print(s)
	a = [0 for i in range(128)]
	for c in s:
		a[ord(c)] ^= 1
	return sum(a) <= 1

print(isPalindromePermutation('bbaa'))
print(isPalindromePermutation('abcd'))
print(isPalindromePermutation('abcdcdb'))

def modify_list(lst):
	lst.append('d')
	lst.append('e')
	print(lst)

a = ['a','b','c']
print(a)
modify_list(a)
print(a)