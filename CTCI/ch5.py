# def mask_between(start,stop):
# 	mask = 0
# 	for i in range(stop-start):
# 		mask <<= 1
# 		mask |= 1
# 	print(bin(mask))
# 	for i in range(start):
# 		mask <<= 1
# 	print(bin(mask))
# 	mask &= 0xffffffff
# 	print(bin(mask))
# 	mask = ~mask
# 	print(bin(mask))
# 	return mask

def insert(m,n,i,j):
	print("M: %s N: %s" % (bin(m), bin(n)))
	mask = (~1 << j+1) | ((1 << i))
	n &= mask
	m <<= i
	n |= m
	print("RESULT: %s" % bin(n))
	return n

def double_to_bin(dbl):
	if dbl < 0 or dbl > 1:
		return None
	else:
		exp = 1
		num = "0."
		while dbl:
			digit = 2**-exp
			print("POWER: -%d\tDIGIT: %f\tNUM: %f" % (exp, digit, dbl))
			if digit <= dbl:
				dbl -= digit
				num += "1"
			else:
				num += "0"
			exp += 1
			if exp > 64:
				print(num)
				return "ERROR"
		return num

def flip_to_win(n):
	longest = 1
	joined = 0
	current = 0
	previous = 0
	while n > 0:
		if n & 1 == 1:
			current += 1
		else:
			joined = 1
			previous = current
			current = 0
		run_length = sum([current, joined, previous])
		longest = run_length if run_length > longest else longest
		n >>= 1
	return longest

def next_nums(n):
	low = high = None
	position = 0
	current_bit = prev_bit = 0
	next_bit = n & 1
	while n >> position > 0:
		prev_bit = current_bit
		current_bit = next_bit
		next_bit = (n>>(position + 1)) & 1
		if current_bit == 1:
			if (position > 0) and (prev_bit == 0) and (low is None):
				low = shift_bit(n, position, -1)
			if next_bit == 0 and high is None:
				high = shift_bit(n, position, 1)
		if low is not None and high is not None:
			break
		position += 1
	return (low, high)

def shift_bit(n, position, delta):
	mask = 1 << position
	n ^= mask
	if delta > 0:
		mask <<= delta
	else:
		mask >>= abs(delta)
	n |= mask
	return n

def print_next_nums(n):
	print("Finding Lower / Higher Numbers for %d (%s)" % (n, bin(n)))
	result = next_nums(n)
	if result[0] is None:
		print("No lower bound with same 1's could be found")
	else:
		print("Lower Number:\t%d\t(%s)" % (result[0], bin(result[0])))
	print("Upper Number:\t%d\t(%s)" % (result[1], bin(result[1])))
	
def flip_to_zero(n):
	print(bin(n))
	while n:
		print("N: %s\tN-1: %s" %(bin(n), bin(n-1)))
		n &= n-1

def swap_bits(num):
	return (num & 0xaaaaaaaa) >> 1 | (num & 0x55555555) << 1

def print_swap_bits(num):
	print("SWAPPING:\t%d\t%s" % (num, bin(num)))
	swapped = swap_bits(num)
	print("SWAPPED: \t%d\t%s" % (swapped, bin(swapped)))
