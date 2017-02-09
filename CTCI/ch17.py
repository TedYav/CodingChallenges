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

"""

	BINODE
	Given structure with pointers to two other nodes, convert BST (of BiNodes) into Double LL of Binodes
		Maintain sorted order

	Easy: In order traversal of tree, build new LL. Problem: not in place. Allocates new data struct
	Better: recursive. Convert node: node.left = tail(convert(node.left)), node.left.right = self etc

	Instead of returning current node, going to return head and tail.
		BEST: allow head and tail as arguments. If none provided, find it via traversal.
		Any node which is left child can use my head.
		Any node which is right child can use my tail.
		Any node which is left child must find own tail.
		Any node which is right child must find own head.

"""

class BiNode:
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right

	def __find_head(self):
		node = self
		while node.left is not None:
			node = node.left
		return node

	def __find_tail(self):
		node = self
		while node.right is not None:
			node = node.right
		return node

	def convert_to_LL(self, head=None, tail=None):
		if head is None: head = self.__find_head()
		if tail is None: tail = self.__find_tail()
		if self.left is not None:
			left_list = self.left.convert_to_LL(head=head)
			self.left = left_list[1]
			self.left.right = self
		if self.right is not None:
			right_list = self.right.convert_to_LL(tail=tail) 
			self.right = right_list[0]
			self.right.left = self
		return (head,tail)

	def __render_tree(self, iter=1):
		out = ""
		if self.left is not None:
			out += self.left.__render_tree(iter+1)
		out += ", " + str(self.value)
		if self.right is not None:
			out += self.right.__render_tree(iter+1)
		return out

	def __render_list(self):
		out = ""
		node = self
		while node.left:
			node = node.left
		while node:
			out += str(node.value) + ","
			node = node.right
		return out

	def print_as_tree(self):
		print(self.__render_tree())

	def print_as_list(self):
		print(self.__render_list())

def test_bi_node():
	root = BiNode(5)
	root.left = BiNode(3)
	root.left.right = BiNode(4)
	root.left.left = BiNode(2)
	root.right = BiNode(7)
	root.right.left = BiNode(6)
	root.right.right = BiNode(8)
	print("ROOT AS TREE: ")
	root.print_as_tree()
	print("ROOT AS LIST: ")
	root.print_as_list()
	print("CONVERTING")
	result = root.convert_to_LL()
	# print("ROOT AS TREE: ") BAD WILL CAUSE INFINITE LOOP!
	# root.print_as_tree()
	print("ROOT AS LIST: ")
	root.print_as_list()

"""

	RESPACE:
		Given string s, and dictionary d:
			divide s into blocks such that number of unmatched characters is minimum.

	NAIVE SOLUTION: try all possible blockings. Exponential time.
	GREEDY SOLUTION: try matching first char, second etc. Doesn't get optimal solution necessarily.
	BEST: Dynamic Programming.
		Step 1: Convert Dictionary into Prefix Trie
		Step 2: Iterate through array to minimize mismatched characters.

		Let F(i) be the minimum number of unmatched characters I can have starting at index i in s.
			If i == n-1: 1 if s_i not in dictionary else 0
			Otherwise:
				If there is a word starting at s_i:
					let w_0...w_j be the length of all the words I can match starting at s_i:
					F(i) == min(F(i + w_j))
				Else:
				F(i+1) + 1
		Return F(0)
"""

class TrieNode:
	def __init__(self, char):
		self.children = {}
		self.char = char
		self.prefix = ''
		self.complete_word = False

class PrefixTrie:
	def __init__(self,words):
		self.__root = TrieNode('')
		for word in words:
			self.add_word(word)

	def add_word(self, word):
		node = self.__root
		word = word.lower()
		# print("ADDING WORD %s" % word)
		for c in word:
			if c not in node.children:
				node.children[c] = TrieNode(c)
				node.children[c].prefix = node.prefix + c
			node = node.children[c]
		node.complete_word = True

	# this is not really the job of the Prefix Trie
	# but putting it outside would expose a lot of implementation
	# this is just an interview problem but I'm just commenting on it
	def get_possible_words(self, s, start_index):
		possible_words = []
		node = self.__root
		for i in range(start_index,len(s)):
			c = s[i]
			if c in node.children:
				node = node.children[c]
				if node.complete_word:
					possible_words.append(s[start_index:i+1])
			else:
				break
		return possible_words

	def print_tree(self):
		stack = [self.__root]
		while stack:
			node = stack.pop()
			print(node.prefix)
			# print(node.children.keys())
			for c in node.children:
				stack.append(node.children[c])


def respace_string(s, words):
	words = PrefixTrie(words)
	n = len(s)
	min_mismatches = [0 for i in range(n+1)]
	spaces = [[] for i in range(n+1)]
	for i in range(n-1, -1 , -1):
		min_mismatches[i] = min_mismatches[i+1] + 1
		spaces[i] = spaces[i+1]
		possible_words = words.get_possible_words(s,i)
		for word in possible_words:
			if min_mismatches[i + len(word)] < min_mismatches[i]:
				min_mismatches[i] = min_mismatches[i + len(word)]

				# could optimize this if desired to avoid unnecessary concatenations
				if len(spaces[i + len(word)]) > 0 and spaces[i + len(word)][0] != i + len(word):
					spaces[i] = [i, i+len(word)] + spaces[i + len(word)]
				else:
					spaces[i] = [i] + spaces[i + len(word)]
	return (add_spaces_to_string(s, spaces[0]), min_mismatches[0])

def add_spaces_to_string(s, spaces):
	output = []
	j = 0
	for i in range(len(s)):
		if j < len(spaces) and spaces[j] == i:
			output.append(' ')
			j += 1
		output.append(s[i])
	return "".join(output)

def test_min_mismatches():
	s = "jesslookedjustliketimherbrother"
	words = ['looked', 'just', 'like', 'her', 'brother']
	print(respace_string(s, words))

"""

	K-Items
	Return first k items from list.

	Strategies:
		If desired in sorted order -- sort and return first 7 (or use min heap)
		If order can be arbitrary -- det select

"""
import random
def det_select_k(arr, k):
	start = 0
	end = len(arr) - 1
	left, middle = 0, 0
	while left + middle < k or left > k:
		pivot = arr[random.randint(start, end)]
		new_left, new_middle = pivot_with_duplicates(arr, pivot, start, end)
		if left + middle < k:
			left = left + middle + new_left # old middle is now included in left
		else: #left > k, we've partitioned left hand side
			left = new_left

		middle = new_middle # middle always the new length

		if left > k:
			start = 0
			end = left
		else:
			start = left + middle
			end = len(arr) - 1
	return arr[:k]

def swap(arr,i,j): arr[i],arr[j] = arr[j],arr[i]

def pivot_with_duplicates(arr, pivot, start, end):
	left = start
	right = end
	middle = left
	while middle <= right:
		if arr[middle] < pivot:
			swap(arr, left, middle)
			middle += 1
			left += 1
		elif arr[middle] > pivot:
			swap(arr, right, middle)
			# know right is bigger now, can move
			right -= 1
		else:
			middle += 1
	return (left - start,right - left + 1)

def test_first_k(k=5):
	arr = [5,4,9,2,3,6,4,4,2,10,23,445,432,32,17]
	# [2, 2, 3, 4, 4, 4, 5, 6, 9, 10, 17, 23, 32, 432, 445]
	print(det_select_k(arr,k))

"""

	LONGEST WORD:
		Stragegy:
			Store all words in dictionary for O(1) lookups
			Sort by length of words
			Check in reverse
			Any time combination found that's composed of other words, append to dict
			Return longest

"""

def longest_word_composed_of_others(words):
	word_map = make_word_map(words)
	words.sort(reverse=True,key=lambda word: len(word))
	# print(words)
	# print(word_map)
	for word in words:
		if is_compound_word(word, word_map):
			print(word)
			# print(word_map)
			return word
	return None

def is_compound_word(word, word_map, original_word = True):
	if len(word) == 0: return True
	elif original_word == False and word in word_map: return True
	else:
		for i in range(1,len(word)):
			if word[:i] in word_map and is_compound_word(word[i:], word_map, False):
				word_map[word] = True
				return True
		return False


def make_word_map(words): return {word: True for word in words}

def test_longest_word():
	words = ['apple', 'app', 'applepie', 'pie', 'cream', 'applecreampie', 'verylongnoncompoundword']
	longest_word_composed_of_others(words)

"""

	MASSEUSE:
		Given lengths of n back to back appointments, return longest amount of time that can be scheduled.
		Given that there must be AT LEAST a 15 minute break between appointments -- adjacent requests cannot be fulfilled

		All are multiples of 15. (Thus no two adjacent ones can be done)

	let F(i) = longest sequence of appointments I can have starting at index i
		= 0, i > n
		= i, i == n
		= max(F(i+2) + a_i, F(i+1))
	return F(0)

"""

def masseuse(appointments):
	n = len(appointments)
	max_time = [0 for i in range(n + 1)]
	max_time[n-1] = appointments[-1]
	for i in range(n-2, -1, -1):
		max_time[i] = max(max_time[i+1], max_time[i+2] + appointments[i])
	return max_time[0]

def masseuse_constant_space(appointments):
	n = len(appointments)
	best_with_current = appointments[-1]
	best_with_next = 0
	best_without_next = 0
	for i in range(n-1, -1, -1):
		best_with_current = max(best_with_next, best_without_next + appointments[i])
		best_without_next = best_with_next
		best_with_next = best_with_current
	return best_with_current

def masseuse_constant_space_forward(appointments):
	n = len(appointments)
	best_with_previous = 0
	best_without_previous = 0
	best_with_current = 0
	for i in range(n):
		best_with_current = max(best_with_previous, best_without_previous + appointments[i])
		best_without_previous = best_with_previous
		best_with_previous = best_with_current
	return best_with_current

def test_masseuse():
	test = [30,15,60,75,45,15,15,45]
	print(masseuse(test))
	print(masseuse_constant_space(test))
	print(masseuse_constant_space_forward(test))


"""

	MULTI SEARCH
		Given string b, array of k smaller strings t, design method to search for all small strings in b

	How long for search to take?
		O(1) ==> O(n^2) to make hash table
		O(len(s)) ==> make a graph of nodes for each suffix of b O(b^2)
		O(b * t) ==> just search b linearly for each string
		O(len(s)) ==> optimized: make trie of smaller strings O(kt) then search for them in bigger word (O(bk))
			==> O(kt + bk)


"""

class TrieNode2:
	def __init__(self, char):
		self.children = {}
		self.complete_word = False
		self.char = char
		self.prefix = ''

class PrefixTrie2:
	def __init__(self,words):
		self.__root = TrieNode2('')
		for word in words:
			self.add_word(word)

	def add_word(self, word):
		node = self.__root
		word = word.lower()
		for c in word:
			if c not in node.children:
				node.children[c] = TrieNode2(c)
				node.children[c].prefix = node.prefix + c
			node = node.children[c]
		node.complete_word = True
		# print(node.prefix)

	def remove_word(self, word):
		node = self.__root
		for c in word:
			node = node.children[c]
		node.complete_word = False

	def get_matches(self, s):
		match = ''
		matches = []
		node = self.__root
		# print(s)
		for c in s:
			if c not in node.children:
				# print("letter %s not found" % c)
				break
			else:
				match += c
				node = node.children[c]
				if node.complete_word: matches.append(match)
		return matches

def find_smaller_in_larger(s, substrings):
	trie = PrefixTrie2(substrings)
	found = {}
	for i in range(len(s)):
		matches = trie.get_matches(s[i:])
		# print(s[i:])
		# print(matches)
		for match in matches:
			if match not in found: found[match] = i
			trie.remove_word(match) # do not match again
	return found

def test_find_smaller_in_larger():
	s = 'mississippi'
	substrings = ['is', 'ip', 'ipp', 'ipx', 'sipp', 'sip', 'pie', 'miiss']
	print(find_smaller_in_larger(s, substrings))

"""

	SHORTEST SUBSEQUENCE:
		Find shortest subarray in longer array that contains all elements of shorter array
		shorter array contains distinct elements

		Solution: use sets. Convert smaller array into set.
			Iterate from begining, record min length from each element needed to have complete set.

"""

def shortest_complete_subsequence(longer, shorter):
	shorter = set(shorter)

	min_length = sys.maxsize
	min_indices = []
	counts = {longer[0]:1}
	j = 0
	for i in range(len(longer)):
		while len(shorter.difference(counts.keys())) > 0:
			j += 1
			if j == len(longer): return min_indices
			else:
				if longer[j] in counts:
					counts[longer[j]] += 1
				else:
					counts[longer[j]] = 1
		if j - i < min_length:
			min_length = j-i
			min_indices = [i,j]
		counts[longer[i]] -= 1
		if counts[longer[i]] == 0:
			del counts[longer[i]]
	return min_indices

def shortest_complete_subsequence_faster(longer, shorter):
	if len(shorter) >= len(longer): return None
	occurence_list = build_occurence_list(longer, shorter)

	# optimization to avoid pop()
	heads = {k:0 for k in occurence_list.keys()}
	min_length = sys.maxsize
	min_indices = []
	start,start_element,end,end_element = get_min_max_heads(occurence_list,heads)
	while start != -1:
		if end - start < min_length:
			min_length = end - start
			min_indices = [start,end]
		heads[start_element] += 1
		start,start_element,end,end_element = get_min_max_heads(occurence_list,heads)
	return min_indices

def get_min_max_heads(occurence_list, heads):
	start = start_element = sys.maxsize
	end = end_element = -1
	for k in occurence_list:
		if heads[k] >= len(occurence_list[k]): return (-1,-1,-1,-1)
		else:
			if occurence_list[k][heads[k]] < start:
				start = occurence_list[k][heads[k]]
				start_element = k
			if occurence_list[k][heads[k]] > end:
				end = occurence_list[k][heads[k]]
				end_element = k
	return (start,start_element,end,end_element)


def build_occurence_list(longer, shorter):
	occurence_list = {i:[] for i in shorter}
	for i in range(len(longer)):
		if longer[i] in occurence_list:
			occurence_list[longer[i]].append(i)
	return occurence_list


import timeit
def test_shortest_complete_subsequence(n=10000, s=500,n_factor=5, times=10):
	shorter = [1,5,9]
	longer = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
	print(shortest_complete_subsequence(longer, shorter))
	print(shortest_complete_subsequence_faster(longer, shorter))
	print("GENERATING LONG SEQUENCES FOR TIMING")
	longer = [random.randint(-n*n_factor, n*n_factor) for i in range(n)]
	shorter = set()
	while len(shorter) < s:
		shorter.add(longer[random.randint(0,n-1)])
	shorter = list(shorter)
	# print(longer)
	# print(shorter)
	print('shortest complete subsequence %s' % shortest_complete_subsequence_faster(longer, shorter))
	def a(): shortest_complete_subsequence(longer, shorter)
	def b(): shortest_complete_subsequence_faster(longer, shorter)
	print("TIMING ORIGINAL VERSION")
	time1 = timeit.timeit(a,number=times)
	print(time1/times)
	print("TIMING \"OPTIMIZED\" VERSION")
	time2 = timeit.timeit(b,number=times)
	print(time2 / times)
	print("SPEEDUP FACTOR: %f" % (time1/time2))

	# OBSERVATION: when n_factor is low (lots of collisions and possible subsequences)
	# Set Based answer out performs optimized list based answer.
	# When there are FEW collisions (very long sequences needed), set based answer DRAMATICALLY
	# underperforms, possibly by factor of ~100


"""

	Find Missing Numbers:
		Single Missing: easy. Sum it up. Subtract from expected sum.
		Double Missing: 
			sum it up. Find single missing number. Partition around missing//2. Find missing # in smaller half.
		Double Missing w/out modifying array:
			sum it. sum squares. Solve quadratic formula.

"""
import math
def find_missing_numbers_non_mutating(arr):
	missing = find_missing_number(arr,num_missing=2)
	missing_squares = sum(map(lambda x: x**2, range(1,len(arr)+3))) - sum(map(lambda x: x**2, arr))
	# x + y = missing
	# x^2 + y^2 = missing_squares
	"""
		y = missing - x
		x^2 + (missing - x)^2 = missing_squares
		x^2 + missing^2 -2(missing * x) + x^2 = missing_squares
		2x^2 -2*missing*x + missing^2 - missing_squares = 0
		x = [-b +/- sqrt(b^2 - 4ac)]/2a
	"""
	a = 2
	b = -2 * missing
	c = missing**2 - missing_squares
	first = (-b - math.sqrt(b**2 - 4*a*c))//(2*a)
	second = missing - first
	return (int(first), int(second))


def find_missing_numbers(arr):
	total_missing = find_missing_number(arr,2)
	i = pivot(arr,total_missing//2)
	if i > len(arr)//2:
		first = find_missing_number(arr[i:],1,i+2)
	else:
		first = find_missing_number(arr[:i],1)
	second = total_missing - first
	return (first,second)

def pivot(arr,p):
	start,end = 0,len(arr) - 1
	left, right = start, end
	while right > left:
		while arr[left] <= p and left < end: left += 1
		while arr[right] > p and right > left: right -= 1
		if right > left:
			swap(arr,left,right)
			left += 1
			right -= 1
	return left

def find_missing_number(arr,num_missing=1,start=1):
	length = len(arr) + num_missing
	return expected_sum(length,start) - sum(arr)

def expected_sum(end,start=1): 
	return (((end)*(end+1))//2) - (((start*(start-1)))//2)

"""

	CONTINUOUS MEDIAN:
		Given numbers, write function to continuously maintain median value as we add values

	STRATEGY:
		Encapsulate in class (to maintain state)
		Use min-heap for numbers larger than median, max-queue for numbers less than or equal to median.
		When we get a new number:: less than median? add to smaller queue. Greater than median? Add to larger queue.
		If difference in size is greater than 1: pop element from smaller and add to larger. (Smaller will ALWAYS be at least as large)

"""

import heapq
class MedianManager:
	def __init__(self):
		self.below = []
		self.above = []
		self.median = None

	# major kludge: negate values for min heap
	def add_value(self,value):
		if self.median is None:
			self.median = value
			heapq.heappush(self.below,-value)
		else:
			if value <= self.median:
				heapq.heappush(self.below,-value)
			else:
				heapq.heappush(self.above,value)
			if len(self.below) - len(self.above) > 1:
				heapq.heappush(self.above,-heapq.heappop(self.below))
			elif len(self.above) > len(self.below):
				heapq.heappush(self.below,-heapq.heappop(self.above))
			self.median = -self.below[0] if len(self.below) > len(self.above) else ((-1*self.below[0]) + self.above[0])/2
			assert len(self.below) - len(self.above) in [0,1]
			# print(self.above)
			# print(self.below)

def test_median_manager(n=50):
	arr = [random.randint(0,n) for i in range(n)]
	mm = MedianManager()
	print(arr)
	for i in range(n):
		mm.add_value(arr[i])
		print("MEDIAN OF: %s IS %.0f" % (str(sorted(arr[:i+1])),mm.median))

"""

	HISTOGRAM VOLUME :: given heights of unit width histograms, calculate how much water they would hold.

	STRATEGY:
		Set c_max = 0
		Set c_max_index = -1
		Set overall_max = 0
		Set next_max = {}
		Iterate forward through array.
			For each non-zero histogram:
				If greater than current max, update current max, and store current index / height in next_max[previous]
			Update overall max
		Iterate backwards.
			Do same thing, except store previous max in current whenever larger one is encountered.
			As soon as histogram encountered of height overall_max, break.
		Iterate forwards:
			For each histogram, set current_max. Look up next_max. Subtract heights of all histograms in between.
		Sum volume.
		Return

	TIME COMPLEXITY: O(n) --> 3 iterations.
"""

def histogram_fill(histograms):
	maximums = find_maximums(histograms)
	if len(maximums) <= 1: return 0
	current_max_index,current_max = maximums[0]
	next_max_index, next_max = maximums[current_max_index]
	current_area_to_subtract = 0
	area = 0
	for i in range(current_max_index, len(histograms)):
		if i < next_max_index and i != current_max_index:
			current_area_to_subtract += histograms[i]
		elif i == next_max_index:
			area += calculate_area(current_max,current_max_index,next_max,next_max_index,current_area_to_subtract)
			current_max_index, current_max = next_max_index, next_max
			current_area_to_subtract = 0
			if current_max_index in maximums:
				next_max_index, next_max = maximums[current_max_index]
			else:
				break
	return area

def calculate_area(height1, index1, height2, index2, area_to_subtract):
	return (min(height1,height2) * (index2 - index1 - 1) - area_to_subtract)

def find_maximums(histograms):
	maximums = {}

	current_max = 0
	current_max_index = -1
	overall_max = 0
	# iterate forwards
	for i in range(len(histograms)):
		if histograms[i] > 0 and histograms[i] >= current_max:
			if current_max_index >= 0:
				maximums[current_max_index] = (i,histograms[i])
			else:
				maximums[0] = (i, histograms[i])
			current_max = histograms[i]
			current_max_index = i
			if current_max > overall_max:
				overall_max = current_max
	
	# iterate backwards
	current_max = 0
	current_max_index = -1
	for i in range(len(histograms)-1,-1,-1):
		if histograms[i] > 0 and histograms[i] >= current_max:
			if current_max_index >= 0:
				maximums[i] = (current_max_index,current_max)
			current_max = histograms[i]
			current_max_index = i
			if current_max == overall_max:
				break
	return maximums

def test_histogram_fill():
	histograms = [0,0,4,0,0,6,0,0,3,0,5,0,1,0,0,0]
	print("TESTING: %s EXPECTED: %d" % (str(histograms),26))
	print(histogram_fill(histograms))
	histograms = [0,0,4,0,0,6,0,0,3,0,8,0,2,0,5,2,0,3,0,0]
	print("TESTING: %s EXPECTED: %d" % (str(histograms),46))
	print(histogram_fill(histograms))



"""

	WORD TRANSFORMER:
		Given two words of equal length in dictionary, transform one into another changing one letter at a time.

	STRATEGY:
		NAIVE: Look over whole dictionary for words one character away from current. Make list. For each, iterate again.
				SLOW --> huge growth in time.
		BETTER:
			Map wildcard words together. Use BFS from start and end.

"""
from functools import reduce
import queue

class WordTransformer:
	def __init__(self, dictionary):
		self.dictionary = dictionary
		self.wildcard_map = self.build_wildcard_map(dictionary)
		# print(self.wildcard_map)

	def build_wildcard_map(self, dictionary):
		wildcard_map = {}
		for i in range(len(dictionary)):
			word = dictionary[i]
			# print(word)
			wildcards = self.make_wildcards(word)
			for wildcard in wildcards:
				if wildcard in wildcard_map: wildcard_map[wildcard].append(word)
				else: wildcard_map[wildcard] = [word]
		return wildcard_map

	def wildcard_matches(self,word,wildcard):
		if len(word) != len(wildcard): return False
		else:
			for i in range(len(word)):
				if word[i] != wildcard[i] and wildcard[i] != '?':
					return False
			return True

	def make_wildcards(self,word): return [self.make_wildcard(word,j) for j in range(len(word))]

	def make_wildcard(self,word,index): return word[:index] + '?' + word[index+1:]

	# def branch(self, word): return list(set(reduce(lambda l1, l2: l1 + l2, map(lambda wildcard: self.wildcard_map[wildcard], self.make_wildcards(word)))))

	# do BFS from first to second --> make function to convert wildcard map into graph
	def transform(self,word1,word2):
		if len(word1) == len(word2):
			def branch(word): return list(set(filter(lambda w: w != word, reduce(lambda l1, l2: l1 + l2, map(lambda wildcard: self.wildcard_map[wildcard], self.make_wildcards(word))))))
			bfs_tree = IterativeBFS(word1, word2, branch)
			result = []
			while len(result) == 0: result = bfs_tree.iterate()
			print(result)

class Node:
	def __init__(self, value, pred=None):
		self.value = value
		self.pred = pred
		self.children = []

	def add_child(self, child):
		self.children.append(child)
		child.pred = self

	def __str__(self):
		return "NODE: %s \tPRED: %s" % (self.value, (self.pred.value if self.pred is not None else "-"))

	def __repr__(self):
		return str(self)

class IterativeBFS:
	def __init__(self,start,end,branch_function):
		self.__start = Node(start)
		self.__end = Node(end)

		self.__start_queue = queue.Queue()
		self.__start_queue.put(self.__start)

		self.__end_queue = queue.Queue()
		self.__end_queue.put(self.__end)

		self.__start_node_table = {start: self.__start}
		self.__end_node_table = {end: self.__end}
		self.__branch_function = branch_function

	def iterate(self):
		new_start_queue = queue.Queue()
		new_end_queue = queue.Queue()
		while not self.__start_queue.empty():
			node = self.__start_queue.get()
			# print(node)
			next_nodes = self.__branch_function(node.value)
			# print("NEXT NODES: %s" % str(next_nodes))
			for value in next_nodes:
				if value in self.__end_node_table:
					return self.__make_path(node,self.__end_node_table[value])
				else:
					new_node = Node(value)
					node.add_child(new_node)
					new_start_queue.put(new_node)
					self.__start_node_table[new_node.value] = new_node

		while not self.__end_queue.empty():
			node = self.__end_queue.get()
			# print(node)
			next_nodes = self.__branch_function(node.value)
			# print("NEXT NODES: %s" % str(next_nodes))
			for value in next_nodes:
				if value in self.__start_node_table:
					return self.__make_path(self.__start_node_table[value], node)
				else:
					new_node = Node(value)
					node.add_child(new_node)
					new_end_queue.put(new_node)
					self.__end_node_table[new_node.value] = new_node

		self.__start_queue = new_start_queue
		self.__end_queue = new_end_queue
		return []

	def __make_path(self, to_start,to_end):
		left_part = []
		right_part = []
		node = to_start
		while node:
			left_part.append(node.value)
			node = node.pred
		node = to_end
		while node:
			right_part.append(node.value)
			node = node.pred
		return left_part[::-1] + right_part

def test_word_transformer():
	dictionary = ["damp","lamp","limp","lime","like","lick","love","dump","pump"]
	wt = WordTransformer(dictionary)
	return wt

"""

	MAX SQUARE MATRIX:
		Given square matrix (nxn) -- return largest subsquare (mxm) s.t. all blocks in the border are black.

	STRATEGY:
		Convert matrix so that 0 represents black, 1 represents white 
		Precalculate number of 1's lying to the right of a current square, not including it
		Precalculate number of 0's lying below a current square, not including it

		Iterate through squares, look at corners. Pick max_size.

		O(N^3) Complexity -- once we find a square we don't look at any smaller ones.
"""

def max_square_matrix(matrix):
	if len(matrix) != len(matrix[0]): return None
	else:
		n = len(matrix)
		zero_counts = precalculate_zeroes(matrix)
		max_size = 1
		max_corner = None # upper left corner
		for row in range(n):
			if n-row < max_size: break
			for col in range(n):
				if n-col < max_size: break
				max_possible_size = largest_square_at(matrix,row,col,zero_counts, max_size)
				if max_possible_size > max_size:
					max_size = max_possible_size
					max_corner = (row,col)
		return (max_corner, max_size)

def precalculate_zeroes(matrix):
	zeroes = [[(0,0) for j in matrix[0]] for i in matrix]
	for row in range(len(matrix)-1,-1,-1):
		for col in range(len(matrix[0])-1,-1,-1):
			if matrix[row][col] == 0:
				right_zeroes = (zeroes[row][col + 1][1] if col < len(matrix[0]) - 1 else 0) + 1
				bottom_zeroes = (zeroes[row + 1][col][0] if row < len(matrix) - 1 else 0) + 1
				zeroes[row][col] = (bottom_zeroes, right_zeroes) # to correspond to rows, columns
	return zeroes

def largest_square_at(matrix,row,col,zero_counts, max_size):
	if matrix[row][col] == 0:
		test_size = min(zero_counts[row][col])
		while test_size > max_size:
			test_right_zeroes = zero_counts[row + test_size - 1][col][1]
			test_bottom_zeroes = zero_counts[row][col + test_size - 1][0]
			if test_right_zeroes >= test_size and test_bottom_zeroes >= test_size:
				max_size = test_size
			test_size -= 1
	return max_size

def test_max_square_matrix():
	matrix =   [[1,1,1,0,1],\
				[0,0,0,0,0],\
				[1,0,1,1,0],\
				[0,0,1,0,0],\
				[1,0,0,0,0]]
	print(max_square_matrix(matrix))


"""

	MAXIMUM SUBMATRIX:
		Given NxN matrix, return maximum sum that can be obtained from any submatrix

	BRUTE FORCE: O(n^6) ==> try all pairs and calculate sum. N^4 Pairs, N^2 time per calculation.
	
	BETTER: precalculate sums for all pairs O(n^4), return max

	BEST: calculate all sums starting from top left: O(n^2)
			Use sums to calculate sum for any given submatrix: O(1)
			Calculate best submatrix for every pair of rows r_1 and r_2: O(n^2) * O(n) = O(n^3)
			To find best sum in O(n) time, store sum at each column, and min sum up to that point.
			Initialize min sum to zero.
			Store max of value - min_sum for each pair of rows. Return maximum.

			OVERALL: O(n^3)

"""

def maximum_submatrix(matrix):
	if len(matrix) != len(matrix[0]): return -1
	else:
		n = len(matrix)
		sums = precalculate_sums(matrix)
		max_sum = -sys.maxsize
		max_corners = []
		for row1 in range(n):
			for row2 in range(row1,n):
				current_max,corner1,corner2 = max_sum_for_rows(matrix,row1,row2,sums)
				if current_max > max_sum:
					max_sum = current_max
					max_corners = (corner1,corner2)
		return (max_sum, max_corners)

def precalculate_sums(matrix):
	sums = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if row - 1 >= 0:
				sums[row][col] += sums[row - 1][col]
			if col - 1 >= 0:
				sums[row][col] += sums[row][col - 1]
			if row - 1 >= 0 and col - 1 >= 0:
				sums[row][col] -= sums[row - 1][col - 1] #double counted
	return sums

def max_sum_for_rows(matrix,row1,row2,sums):
	cols = len(matrix[0])
	max_sum = -sys.maxsize
	max_column = 0
	min_sum = 0
	min_column = -1
	
	for col in range(0,cols):
		current_sum = calculate_sum(sums,row1,row2,0,col)
		if current_sum - min_sum > max_sum:
			max_sum = current_sum - min_sum
			max_column = col
		if current_sum < min_sum:
			min_sum = current_sum
			min_column = col

	corner2 = (row2,max_column)
	corner1 = (row1,min_column+1)
	return (max_sum,corner1,corner2)

# expect col2 > col1, row2 > row1, could check input, not going to
def calculate_sum(sums,row1,row2,col1,col2):
	total = sums[row2][col2]
	if col1 > 0:
		total -= sums[row2][col1-1]
	if row1 > 0:
		total -= sums[row1-1][col2]
	if row1 > 0 and col1 > 0:
		total += sums[row1-1][col1-1]
	return total

def test_maximum_submatrix():
	matrix =   [[-1,-1,-1],\
				[2,2,2],\
				[3,3,3]]
	# should be 15
	print(maximum_submatrix(matrix))

"""

		WORD RECTANGLE:
			Given a dictionary of valid words,
			return largest matrix of letters,
			such that each row (left to right) and each column (top to bottom) is in dictionary.

		Brute Force: try every letter. Let n be longest word. We have 26^(n^n). Very stupid.
		Less Stupid Brute Force: Try every arrangement of words of every size. O(sum(2^n_i))
		Optimal: 
			*Group words by length
			*Try to create a rectangle of maximum length for each.
				*Create prefix tries of words for given length (create lazily)
				*Use prefix tries to short circuit
				*Use DFS to try to build a rectangle
			*Return first valid rectangle

"""

class WordTrieNode:
	def __init__(self, char='', parent=None, complete_word = False):
		self.char = char
		self.parent = parent
		self.prefix = '' if self.parent is None else self.parent.prefix + self.char
		self.complete_word = complete_word
		self.children = {}

	def get_child_letters(self):
		return self.children.keys()

class WordTrie:
	def __init__(self, words):
		self.__root = WordTrieNode()
		self.__words = words # store words in original form as well -> don't have to traverse tree to iterate
		for word in words:
			self.add_word(word)

	def add_word(self,word):
		word = word.lower()
		node = self.__root
		for c in word:
			if c not in node.children:
				node.children[c] = WordTrieNode(c,node)
			node = node.children[c]
		node.complete_word = True

	def get_next_letters(self,prefix):
		node = self.__root
		for c in prefix:
			if c not in node.children: return []
			else:
				node = node.children[c]
		return node.children.keys()

	def get_possible_words(self,possible_letters):
		possible_prefixes = []
		for i in range(len(possible_letters)):
			if len(possible_letters[i]) == 0:
				return [] # can't make any words if no letters for some position
			else:
				possible_prefixes.append([])
				if i > 0:
					if len(possible_prefixes[i-1]) == 0:
						return []
					else:
						for prefix in possible_prefixes[i-1]:
							next_letters = set(self.get_next_letters(prefix)).intersection(possible_letters[i])
							if len(next_letters) > 0:
								possible_prefixes[i].extend([prefix + c for c in next_letters])
				else:
					possible_prefixes[i].extend([c for c in possible_letters[i] if c in self.__root.children])
		return possible_prefixes[-1]

	def __iter__(self):
		return iter(self.__words)

	def __str__(self):
		return "\n".join(self.__to_array(self.__root))

	def __to_array(self,node):
		result = []
		if node.complete_word:
			result.append(node.char)
		for c in node.children:
			for s in self.__to_array(node.children[c]):
				result.append(node.char + s)
		return result


class WordRectangleBuilder:
	def __init__(self, dictionary):
		self.__dictionary = dictionary
		self.__words_of_length = self.__split_dictionary_by_length(dictionary)
		self.__max_length = max(self.__words_of_length.keys())
		self.__tries = {}

	def __split_dictionary_by_length(self, dictionary):
		words = {}
		for word in dictionary:
			length = len(word)
			if length in words:
				words[length].add(word)
			else:
				words[length] = set([word])
		return words

	def make_word_rectangle(self, max_height=None,max_width=None):
		if max_height is None: max_height = self.__max_length
		if max_width is None: max_width = self.__max_length
		dimensions = [(width,height) for width in range(1,max_width+1) for height in range(1,max_height+1)]
		dimensions.sort(reverse=True,key=lambda d: d[0]*d[1])
		for width,height in dimensions:
			word_rectangle = self.__build_rectangle(width,height)
			if word_rectangle: return self.__format_rectangle(word_rectangle)
		return []

	def __format_rectangle(self, word_rectangle):
		return "\n".join(["".join(row) for row in word_rectangle])

	def __build_rectangle(self,width,height):
		vertical_words = self.__tries.get(height,self.__make_trie(height))
		horizontal_words = self.__tries.get(width, self.__make_trie(width))
		if not vertical_words or not horizontal_words: return []
		else:
			# strategy: add first word horizontally arbitrarily
			# add additional words using trie: get possible letter for each position in next row
			# filter through horizontal trie to eliminate bad possibilities
			for word in horizontal_words:
				word_rectangle = self.__add_layers([list(word)],horizontal_words,vertical_words,height)
				if len(word_rectangle) == height: return word_rectangle
			return []
	
	def __add_layers(self,word_rectangle,horizontal_words,vertical_words,height):
		return self.__add_layer(1,word_rectangle,horizontal_words,vertical_words,height)

	def __add_layer(self,layer,word_rectangle,horizontal_words, vertical_words, height):
		if layer == height:
			return word_rectangle
		else:
			possible_letters = []
			for i in range(len(word_rectangle[0])):
				prefix = [word_rectangle[j][i] for j in range(layer)]
				possible_letters.append(set(vertical_words.get_next_letters(prefix)))
			possible_words = horizontal_words.get_possible_words(possible_letters)
			for word in possible_words:
				word_rectangle.append(list(word))
				word_rectangle = self.__add_layer(layer+1,word_rectangle,horizontal_words,vertical_words,height)
				if len(word_rectangle) == height: break
				else: word_rectangle.pop()
			return word_rectangle

	def __make_trie(self, length):
		if length not in self.__words_of_length: return []
		else:
			if length not in self.__tries: self.__tries[length] = WordTrie(self.__words_of_length[length])
			return self.__tries[length]


"""
GOAL:

slam
nice
over
west

cat
are
pea

"""

def test_word_rectangle_builder():
	dictionary = [
		'slam',
		'nice',
		'over',
		'west',
		'snow',
		'live',
		'aces',
		'mert',
		'cat',
		'are',
		'pea',
		'cap',
		'are',
		'tea',
		'type',
		'like',
		'lair',
		'lion',
		'tip',
		'tac',
		'toe',
		'art'
	]
	wrb = WordRectangleBuilder(dictionary)
	word_rectangle = wrb.make_word_rectangle()
	print(word_rectangle)
	return wrb

"""

	SPARSE SIMILARITY:
		Given list of documents (ID + array of integers),
		Return list of pairs of documents along with similarity #: | A intersect B | / | A union B |
		Only list document pairs where similarity > 0

		It is expected that most documents have similarity = 0

	STRATEGY:
	Brute Force: Examine all pairs. Takes O((2^n) * m) where n is number of documents. m is length of longest doc.
	Optimal Strategy: (not very space efficient):
		* Hash all elements in all documents, listing documents where they occur
		* Whenever a collision is found, hash all colliding pairs in hash of pairs -> elements in intersection
		* Iterate through pairs, printing similarity as (size of intersection)/(size of set A + size of set B - size of intersection)

		Time Complexity: O(nm) for initial hashing, O(ps) for pair hashing and output where p is number of pairs, s is elements of largest intersection

		Cannot do better. We have to read all elements (takes O(mn)) and print all pairs (take O(ps))

"""

def sparse_similarity(documents):
	pairs = find_pairs(documents)
	output = similarity_header()
	for doc1,doc2 in pairs:
		output += render_pair_similarity(doc1,doc2,documents,pairs[(doc1,doc2)])
	return output

def similarity_header():
	return "ID1\tID2\tSIMILARITY\n"

def render_pair_similarity(id1,id2,documents,intersection):
	return "%d\t%d\t%.4f\n" % (id1,id2,similarity(documents[id1],documents[id2],intersection))

def similarity(doc1,doc2,intersection):
	return len(intersection)/(len(doc1)+len(doc2)-len(intersection))

def find_pairs(documents):
	element_hash = {}
	pair_hash = {}
	for document_id in documents:
		for element in documents[document_id]:
			if element in element_hash:
				update_pair_hash(pair_hash,element,document_id,element_hash[element])
				element_hash[element].append(document_id)
			else:
				element_hash[element] = [document_id]
	return pair_hash

def update_pair_hash(pair_hash,element,origin_id,doc_ids_to_pair):
	for complement_id in doc_ids_to_pair:
		pair = (origin_id,complement_id) if origin_id < complement_id else (complement_id,origin_id)
		if pair in pair_hash:
			pair_hash[pair].append(element)
		else:
			pair_hash[pair] = [element]

def test_sparse_similarity():
	documents = {
		13: [14,15,100,9,3],
		16:	[32,1,9,3,5],
		19: [15,29,2,6,8,7],
		24: [7,10]
	}
	result = sparse_similarity(documents)
	print(result)