# could add special case for negatives

def binary_add_slow(num1, num2):
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

"""

	BINARY ADD:
		Add two numbers, no + (or other arithmetic operations)

	By definition, we add a binary number by doing a^b.
		This will set all 0's to 1 such that a number is the sum of both inputs.
		HOWEVER, it will set all places where BOTH are 1 to 0.
		Thus, we must add again with the carry bits, which is (a&b << 1).
		We do this until there are no bits to carry :)


	This can be done recursively, as above, or with a stack, as below:

"""

def binary_add(num1, num2):
	if min(num1, num2) < 0: return -1
	stack = [(num1, num2)]
	while stack:
		num1,num2 = stack.pop()
		if num1 == 0: return num2
		stack.append(((num1&num2) << 1, num1 ^ num2))


"""

	SHUFFLE:
		Shuffle a deck of cards perfectly. May use random number function.

	SOLUTIONS:
		Naive: Random(1-52), adjust, Random(1-51), adjust, etc.
			O(n^2) because we have to keep adjusting array. WORKS but too slow. Can we do better?

		YES
		Better solution:
			Create new array.
			Add cards to it one by one.
			On each iteration, random a number from 1 to i.
				Swap card with position i
			Return deck.

			Results in random order, but takes O(n) time and O(n) space complexity.

"""
import random

def swap(arr, i, j): 
	arr[i],arr[j] = arr[j],arr[i]

def shuffle(deck):
	if len(deck) != 52: return deck
	else:
		output = []
		for i in range(52):
			output.append(deck[i])
			j = random.randint(0,i)
			if i != j:
				swap(output,i,j)
		return output

def test_shuffle(iterations=10000):
	counts = {k:0 for k in range(52)}
	total = 0
	for i in range(iterations):
		deck = [i for i in range(52)]
		deck = shuffle(deck)
		for j in range(52):
			counts[j] += deck[j]
			total += deck[j]
	print({k:"%.2f%%" % (v/(total//100)) for k,v in counts.items()})

"""

	RANDOM SET
		Randomly generate set of m integers from array of size n. All must have equal probability.

	Strategy: Shuffle, return left m

"""

def random_set(arr, m):
	if m > len(arr): return []
	elif m == len(arr): return arr
	else:
		output = arr[:m]
		for i in range(m,len(arr)):
			k = random.randint(0,len(arr)-1)
			if k < m:
				output[k] = arr[i]
		return output

"""

	MISSING NUMBER:
		Can only read a number by accessing ith bit in constant time.
		BUT WE CAN move the items into different lists and such in standard amounts of time

	STRATEGY:
		We can know the expected counts for each bit in missing number.
		Thus if we count them, we can iterate on progressivel smaller lists to narrow down on missing #.

"""

class BitInteger:
	def __init__(self, value):
		self.__value = value

	def get_bit(self,i):
		return (self.__value & (1 << i))>>i

def find_missing_value(bit_ints):
	if not bit_ints: return 0
	else:
		n = len(bit_ints)
		expected_sum = (n*(n+1))//2
		current = bit_ints
		result = []
		for bit in range(bits_in(n)):
			zeroes = []
			ones = []
			expected_ones = expected_ones(n,bit,result)
			expected_zeroes = (n+1) - expected_ones 
			for bit_int in current:
				if bit_int.get(bit) == 1:
					ones.append(bit_int)
				else:
					zeroes.append(bit_int)
			if len(ones) == expected_ones:
				result.append[0]
				current = zeroes[0]


"""

	LETTERS AND NUMBERS:
		given array filled w/letters and numbers, find longest subarray w/equal letters and numbers

	Naive: check all subarrays. N^2 subarrays (n^2 points i,j to start), N operations to count, N^3

	WHAT IF: count whole array
	THEN count from either side adding one element each time and logging all the counts in arrays left and right
		N counts in each
	WE can find one or two which will make the number of elements equal. 
	Comparing pairs: N^2
		But if they're in dicts...
	WHAT IF WE STORE THEM AS DIFFERENTIALS rather than raw numbers
		So (8,8) is (0,0) because removing 8 numbers and 8 letters does not change the count.
			(10,8) is (2,0)
		THEN we can quickly look up options for a given differential.
	N comparisons, because shortest is ALWAYS going to be at the front of the list.
	Just check for each differential, check each list. Return min removals from each size to equalize.

	For each differential, we store minimum length needed achieve it by removing.

	If len(d1) + len(d2) > len(arr), find another one. Return n - min(len(d1) + len(d2))

"""

import sys
def max_equal_length(arr):
	overall_differential, right_differentials, left_differentials = calculate_differentials(arr)
	return find_minimum_differential(overall_differential, left_differentials, right_differentials, len(arr))

def calculate_differentials(arr):
	letters = [chr(c) for c in range(ord('a'),ord('z')+1)]
	left_differentials = {(0,0):0}
	right_differentials = {(0,0):0}
	right_counts = [0,0]
	left_counts = [0,0]
	for i in range(len(arr)):
		# left count
		if arr[i] in letters:
			left_counts[0] += 1
		else:
			left_counts[1] += 1
		left_differential = (left_counts[0] - min(left_counts), left_counts[1]-min(left_counts))
		if left_differential not in left_differentials:
			left_differentials[left_differential] = i

		# right count
		if arr[n - i - 1] in letters:
			right_counts[0] += 1
		else:
			right_counts[1] += 1
		right_differental = (right_counts[0] - min(right_counts), right_counts[1]-min(right_counts))
		if right_differental not in right_differentials:
			right_differentials[right_differental] = i

	overall_differential = (right_counts[0] - min(right_counts), right_counts[1] - min(right_counts))
	return (overall_differential, right_differentials, left_differentials)

def find_minimum_differential(overall_differential, left, right, n):
	if sum(overall_differential) == 0: return n
	else:
		min_difference = sys.maxsize

		if overall_differential in left and left[overall_differential] < min_difference: min_difference = left[overall_differential]
		if overall_differential in right and right[overall_differential] < min_difference: min_difference = right[overall_differential]

		for left_differential in left:
			if left_differential != overall_differential:
				right_differential = (overall_differential[0] - left_differential[0], overall_differential[1] - left_differential[1])
				right_differential = (right_differential[0] - min(right_differential), right_differential[1] - min(right_differential))
				if right_differential in right:
					if left[left_differential] + right[right_differential] < min_difference:
						min_difference = left[left_differential] + right[right_differential]

		return n - min_difference if min_difference <= n else 0

"""

	COUNT OF 2's
		between 0 and n:
		For every ten, we have one 2
		for every 100, we have one 2
		...
		SO: n/10 + n/100 + n/1000
		 if decimal >= .2, we round up count to next number

"""

from math import ceil, floor
from decimal import *

def count_2s(n):
	num_twos = 0
	pow = 1
	while n//10**(pow - 1) > 0:
		num_twos += cutoff_round(Decimal(n)/Decimal(10**pow),Decimal(1)/Decimal(5))
		pow += 1
	return num_twos

def cutoff_round(num, cutoff):
	return ceil(num) if num - floor(num) >= cutoff else floor(num)

"""

	BABY NAMES:
	Input: Hash table of names and counts
		   List of tuples of name synonyms


	NAIVE: loop through all name pairs n times (n name pairs), and put into lists, then sum

	BETTER:

	BEST: Dictionary of Name: Set
		Iterate through name pairs. For each, combine into set, add to dictionary twice -- once for each name.
		For each additional entry, if it's already in dict, add to set, and duplicate set for new key
		Then read all the sets, and use them to combine counts from original list.

"""

def baby_names(frequencies, synonyms):
	name_sets = build_name_sets(synonyms)
	final_frequencies = combine_frequencies(frequencies, name_sets)
	return final_frequencies

# ISSUE: need to add to all sets containing a name... :(
def build_name_sets(synonyms):
	set_map = {}
	for pair in synonyms:
		set1 = set_map.get(pair[0],set([pair[0]]))
		set2 = set_map.get(pair[1], set([pair[1]]))
		result = set1.union(set2)
		set_map[pair[0]] = result
		set_map[pair[1]] = result
		print(set_map)
	return set_map

def combine_frequencies(frequencies, name_sets):
	output = {}
	for name in frequencies:
		# delete entries that we've used
		if name in name_sets:
			synonyms = name_sets[name]
			output[name] = 0
			for synonym in synonyms:
				output[name] += frequencies.get(synonym,0)
				del name_sets[synonym]
	return output

def test_baby_names():
	names = {'John': 15, 'Jon': 12, 'Chris':13, 'Kris':4,'Christopher':19}
	synonyms = [('Jon','John'), ('John', 'Johnny'), ('Chris','Kris'), ('Chris','Christopher')]
	print(baby_names(names, synonyms))

"""

	CIRCUS TOWER:
		Given list of heights, weights of circus performers, calculate largest number of people we can stack
		Each person must be strictly shorter and lighter than person underneath.

	NAIVE: try all possible arrangements, see which work. This is N! BAD!
	Better:
		1. Sort by height and weight
		2. Iterate backwards through list, storing max # that can be stacked INCLUDING this person
			Return largest item in array
"""

class Performer:
	def __init__(self, height, weight):
		self.height = height
		self.weight = weight

	def __lt__(self, other):
		return self.height < other.height and self.weight < other.weight

	def __gt__(self, other):
		return self.height > other.height and self.weight > other.weight

def largest_circus_tower(performers):
	if not performers: return 0
	else:
		performers = list(map(lambda t: Performer(t[0], t[1]), performers))
		performers.sort()
		performers = performers[::-1]
		tallest_stacks = [0 for i in range(len(performers))]
		for i in range(len(performers) - 1, -1, -1):
			for j in range(i+1, len(performers)):
				if performers[i] > performers[j] and tallest_stacks[j] > tallest_stacks[i]:
					tallest_stacks[i] = tallest_stacks[j]
			tallest_stacks[i] += 1
		return max(tallest_stacks)

# O(n^2)
# derive O(nlogn) solution --> min_queue for elements later on in arr :)
# use max_queue, push all elements, pop until found...?

def test_circus_performers():
	performers = [(5,5),(4,4),(3,3),(2,2),(1,1),(4,5),(3,4),(2,7)]
	print(largest_circus_tower(performers))


"""

	Kth Multiple:
		Given a number k, return the kth number such that only prime factors are 3,5,7

	NAIVE: enumerate all until we have more than k, sort, return k'th
		O(klogk)
	BETTER: multiply all by 3, by 5, by 7, then repeat until we have more than k, return k'th. Insert in min queue
		O(klogk)
	BEST: only need to find minimum value of 3 possible values at a time, so don't have to use min queue, can use O(1)
		find min operation between three individual queues.
		O(k)


	GENERALIZED SOLUTION BELOW USING FACTOR MAKER CLASS AND LL QUEUE

"""

import sys

class LLQueue:
	def __init__(self, default=None):
		self.__queue = []
		self.__default = default

	def add(self, value):
		self.__queue.append(value)

	def peek(self):
		if self.__default is not None:
			return self.__queue[0] if len(self.__queue) > 0 else self.__default
		else:
			return self.__queue[0]

	def size(self):
		return len(self.__queue)

	def remove(self):
		return self.__queue.pop(0) if len(self.__queue) > 0 else 0

	def __str__(self):
		return str(self.__queue)

	def __repr__(self):
		return str(self)

class FactorMaker:
	def __init__(self, factors):
		factors = sorted(factors)
		self.__factors = factors
		self.__queues = {}
		for factor in factors:
			self.__queues[factor] = LLQueue(default=sys.maxsize)
		self.__queues[factors[0]].add(1)
		self.get_next()

	def __get_min(self):
		val = sys.maxsize
		fact = self.__factors[0]
		for factor in self.__factors:
			if self.__queues[factor].peek() < val:
				val = self.__queues[factor].peek()
				fact = factor
		return (val,fact)

	def __update_factors(self, val, start_factor):
		if start_factor in self.__factors:
			start_index = self.__factors.index(start_factor)
			self.__queues[start_factor].remove()
			for factor in self.__factors[start_index:]:
				self.__queues[factor].add(val*factor)

	def get_next(self):
		val, factor = self.__get_min()
		self.__update_factors(val, factor)
		return val

def kth_multiple(k, factors=[3,5,7]):
	factor_maker = FactorMaker(factors)
	for i in range(k):
		print(factor_maker.get_next())
