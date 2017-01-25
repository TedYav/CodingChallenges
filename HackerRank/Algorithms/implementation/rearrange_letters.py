def min_rearrangement(word):
	for i in range(len(word)-1, -1, -1):
		swap_char = -1
		for j in range(i+1, len(word)):
			if word[j] > word[i]:
				if swap_char == -1 or ord(word[j]) < ord(word[swap_char]):
					swap_char = j
		if swap_char != -1:
			return ''.join(word[:i] + word[swap_char:swap_char+1] + sorted(word [i+1:swap_char] + word[i:i+1] + word[swap_char+1:]))
	return 'no answer'

t = int(input().strip())
for _ in range(t):
	word = list(input().strip())
	print(min_rearrangement(word))