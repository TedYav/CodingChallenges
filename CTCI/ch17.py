# could add special case for negatives

def binary_add(num1, num2):
	carry = 0
	count = 1
	output_reversed = 0
	output = 0
	cutoff1 = 0 if num1 >= 0 else -1
	cutoff2 = 0 if num2 >= 0 else -1
	while (num1 != cutoff1 or num2 != cutoff2) or carry == 1:
		b1 = num1 & 1
		b2 = num2 & 1
		result = b1 ^ b2
		if carry:
			result ^= carry
		if (result == 0 and (b1 | b2) == 1) or (result==1 and (b1 & b2) == 1):
			carry = 1
		else:
			carry = 0
		output_reversed |= result
		# print("NUM1: %s\tNUM2: %s\t RESULT: %s\tOUTPUT_REVERSED: %s\tCARRY: %s" % (bin(num1), bin(num2), bin(result), bin(output_reversed), bin(carry)))
		output_reversed <<= 1
		count <<= 1
		num1 >>= 1
		num2 >>= 1
	while count != 0:
		output |= output_reversed & 1
		output <<= 1
		output_reversed >>= 1
		count >>= 1
	return output>>1

def binary_add_better(num1, num2):
	if num2 == 0:
		return num1
	else:
		temp_sum = num1 ^ num2
		carry = (num1 & num2) << 1
		return binary_add_better(temp_sum, carry)