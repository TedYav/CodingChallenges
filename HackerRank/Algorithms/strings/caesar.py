
lowercase = [chr(c) for c in range(ord('a'),ord('z')+1)]
uppercase = [chr(c) for c in range(ord('A'),ord('Z')+1)]

def encrypt(char,k):
	if char in uppercase or char in lowercase:
		base_val = ord('A') if char in uppercase else ord('a')
		new_val = (ord(char) - base_val + k) % 26
		return chr(new_val + base_val)
	else:
		return char

n = int(input().strip())
s = input().strip()
k = int(input().strip())

output = []
for c in s:
	output.append(encrypt(c,k))

print("".join(output))