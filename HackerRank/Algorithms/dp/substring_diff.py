def run():
	t = int(input().strip())
	for _ in range(t):
		[limit, string1, string2] = input().split()
		limit = int(limit)
		print(max_length_substring(limit, string1, string2))

def max_length_substring(limit, string1, string2):
	max_length = limit
	length = len(string1)
	offset = 0

	max_length = max_length_at_offset(string1, string2, offset, limit, max_length)

	offset += 1
	while offset + max_length < length:
		max_length = max_length_at_offset(string1, string2, offset, limit, max_length)
		max_length = max_length_at_offset(string2, string1, offset, limit, max_length)
		offset += 1
	return max_length

def max_length_at_offset(string1, string2, offset, limit, max_length):
	next_char = start = mismatches = 0
	# programmatic mismatches
	mismatches = sum([1 if string1[i + offset] != string2[i] else 0 for i in range(0, max_length)])
	next_char = max_length
	while start + max_length + offset  < len(string1):
		if string1[next_char + offset] != string2[next_char]:
			mismatches += 1

		if mismatches > limit and next_char >= start + max_length:
			if string1[start + offset] != string2[start]:
				mismatches -= 1
			start += 1
		
		next_char += 1
		new_length = next_char - start
		if new_length > max_length:
			max_length = new_length

	return max_length

run()
# debug()

def max_length_substring_veryslow(limit, string1, string2):
	max_length = 0
	length = len(string1)
	
	for i in range(length):
		if i + max_length > length: break
		for j in range(length):
			if j + max_length > length: break

			mismatches = 0
			for k in range(length - max(i,j)):
				if string1[i+k] != string2[j+k]:
					mismatches += 1
				if mismatches > limit:
					break
				if k >= max_length:
					max_length = k + 1
	return max_length