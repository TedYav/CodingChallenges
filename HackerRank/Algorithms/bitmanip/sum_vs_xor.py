# addition op: x + y = x ^ y + (x & y << 1), thus we want all y s.t. x & y == 0
# meaning: no bits in common
# so find # of 0 bits less than last bit of n and return 2**that number
n = int(input().strip())
num_zero_bits = 0
while n > 0:
	if n & 1 == 0:
		num_zero_bits += 1
	n >>= 1
print(2**num_zero_bits)
