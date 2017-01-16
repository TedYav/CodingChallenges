modulus = 10**9 + 7

# used for lookup to avoid expensive int conversions
one_digit_multiples = ['0', '8']
two_digit_multiples = [str(i).zfill(2) for i in range(0,100,8)]
odd_nums = [str(i) for i in range(1,10,2)]
even_nums = [str(i) for i in range(0,10,2)]

# counts of any digit which could end a multiple of 8
one_digit_suffixes = {str(k):0 for k in range(0,10,2)}

# lookup table for numbers which should increase odd suffix count
odd_suffix_table = {str(i):[str(j).zfill(2)[1] for j in range(10*i, 10*i+10, 2) if j%8==4] for i in range(10)}

# lookup table for numbers which should increase even suffix count
even_suffix_table = {str(i):[str(j).zfill(2)[1] for j in range(10*i, 10*i+10, 2) if j%8==0] for i in range(10)}

# 4,12,20.... -- suffix for any odd number 1,3,5 to be 3 digit multiple of 8
odd_suffix_count = 0 

# 8, 16, 24... -- suffix for any even number 2,4,6 to be a 3 digit multiple of 8
even_suffix_count = 0

n = int(input().strip())
number = input().strip()

# 2 = # of 3 digit or longer multiples of 8
# 1 = # of 2 digit multiples of 8
# 0 = # of 1 digit multiples of 8
# on each turn we add to these, also accounting for prefixes completed by current number

# initialize counts
counts = [[0 for i in range(3)] for j in range(n)]
# last digit -- only count if it's divisible by 8
counts[n-1][2] = 0
counts[n-1][1] = 0
counts[n-1][0] = 1 if (number[n-1] in one_digit_multiples) else 0

if n>=2:
	# increment suffixes
	if number[n-1] in one_digit_suffixes:
		one_digit_suffixes[number[n-1]] += 1

	# second to last digit -- only count if it can form multiple of 8
	counts[n-2][2] = 0
	counts[n-2][1] = 1 if (number[n-2:] in two_digit_multiples) else 0
	counts[n-2][0] = counts[n-1][0] + (1 if (number[n-2] in one_digit_multiples) else 0)

	# increment one digit suffixes
	if number[n-2] in one_digit_suffixes:
		one_digit_suffixes[number[n-2]] += 1

	# increment longer suffixes
	if number[n-1] in odd_suffix_table[number[n-2]]:
		odd_suffix_count += 1
	elif number[n-1] in even_suffix_table[number[n-2]]:
		even_suffix_count += 1

if n>=3:
	for i in range(n-3, -1, -1):
		
		# update counts
		# 1 digit counts
		counts[i][0] = counts[i+1][0] + (1 if number[i] in one_digit_multiples else 0)
		# 2 digit counts
		# list comprehension is faster than lambda :)
		counts[i][1] = counts[i+1][1] + sum([v for k,v in one_digit_suffixes.items() if k in even_suffix_table[number[i]]])
		# counts[i][1] = counts[i+1][1] + sum(map(lambda t: t[1], filter(lambda k: k[0] in even_suffix_table[number[i]], one_digit_suffixes.items())))

		# 3 digit or greater counts
		# multiply previous 3 digit count by 2, because for every item in there, we can add current number to it
		# then add in all suffixes that would make this number a multiple of 8
		counts[i][2] = ((counts[i+1][2] * 2) + (even_suffix_count if number[i] in even_nums else odd_suffix_count)) % modulus

		# update suffix counts
		for suffix in odd_suffix_table[number[i]]:
			odd_suffix_count += one_digit_suffixes[suffix]
		for suffix in even_suffix_table[number[i]]:
			even_suffix_count += one_digit_suffixes[suffix]
		# update this now so it doesn't mess up other suffix counts
		if number[i] in one_digit_suffixes:
			one_digit_suffixes[number[i]] += 1

print(sum(counts[0])%modulus)