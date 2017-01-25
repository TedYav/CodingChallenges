# iterative merge sort using stack :)
def mergesort(a, cmp=lambda x,y: x<y):
	start = 0
	end = len(a)
	stack = [(start,end)]
	while stack:
		indices = stack.pop()
		# sort operation
		if len(indices) == 2:
			start,end = indices
			middle = (end + start)//2
			if end - start > 1:
				stack.append((start, middle, end))
				stack.append((start, middle))
				stack.append((middle, end))
		# merge operation
		else:
			start,middle,end = indices
			temp = []
			i,j = start,middle
			while i < middle or j < end:
				if i < middle and j < end:
					if cmp(a[i],a[j]):
						temp.append(a[i])
						i += 1
					else:
						temp.append(a[j])
						j += 1
				elif i < middle:
					temp.append(a[i])
					i += 1
				else:
					temp.append(a[j])
					j += 1
			a[start:end] = temp
	print(a)
	return a

# stack based randomized quick sort in place
import random

def quicksort_a(a):
	return quicksort(a, partition_double_counter)

def quicksort_b(a):
	return quicksort(a, partition_single_counter)

def quicksort(a, partition_alg=partition_double_counter):
	stack = [(0,len(a)-1)]
	def swap(i,j): a[i],a[j] = a[j],a[i]
	while stack:
		start, end = stack.pop()
		if end-start > 0:
			pivot_index = partition_alg(a,start,end)
			stack.append((start,pivot_index-1))
			stack.append((pivot_index+1, end))
	print(a)
	return a

def partition_double_counter(arr, left, right):
	pivot_index = random.randint(left,right)
	swap(arr,pivot_index,right)
	pivot = arr[right]
	i,j = left,right-1
	while i<=j:
		while arr[i] <= pivot and i < right: i += 1
		while arr[j] > pivot and j >= i: j -= 1
		if i<j:
			swap(arr,i,j)
			i += 1
			j -= 1
	swap(arr,right,i)
	return i


def partition_single_counter(arr, left, right):
	pivot_index = random.randint(left,right)
	swap(arr,pivot_index,right)
	pivot = arr[right]
	pivot_index = 0
	for i in range(right):
		if arr[i] <= pivot:
			swap(arr,i,pivot_index)
			pivot_index += 1
	swap(arr,pivot_index,right)
	return pivot_index

from functools import reduce
def radix_sort(arr):
	place = 1
	arr_min = min(arr)
	if arr_min < 0:
		arr = [i + abs(arr_min) for i in arr]
	arr_max = max(arr)
	while 10**(place-1) <= arr_max:
		buckets = [[] for i in range(10)]
		for num in arr:
			digit = get_digit(num, place)
			buckets[digit].append(num)
		arr = reduce(lambda x,y: x + y, buckets)
		place += 1
	if arr_min < 0:
		arr = [i - abs(arr_min) for i in arr]
	return arr

def high_speed_bucket_sort(arr, domain):
	domain = sorted(domain)
	buckets = [[] for i in domain]
	for element in arr: buckets[domain.index(element)].append(element)
	return reduce(lambda x,y: x+y, buckets)


def get_digit(num, place):
	if place > 1:
		digit = ((num % (10**place)) - (num % (10**(place-1))))//(10**(place-1))
	else:
		digit = num % 10
	return digit

def quicksort_alternate(arr, left=None, right=None):
	if left is None and right is None:
		left,right = 0,len(arr) - 1
	if right - left > 0:
		index = partition(arr, left, right)
		quicksort_alternate(arr, left, index-1)
		quicksort_alternate(arr, index + 1, right)
		return arr

def partition(arr, left, right):
	def swap(i,j): arr[i],arr[j] = arr[j],arr[i]
	if right-left > 0:
		pivot = random.randint(left,right)
		swap(pivot, right)
		pivot = arr[right]
		i,j = left,right-1
		while i<=j:
			while arr[i] <= pivot and i < right: i += 1 
			while arr[j] > pivot and j >= i: j -= 1
			if i < j:
				swap(i,j)
				i += 1
				j -= 1
		swap(right,i)
		return i


def book_quicksort(arr, left=None, right=None):
	if left is None and right is None:
		left, right = 0, len(arr)-1

	index = book_partition(arr, left, right)
	if left < index - 1:
		book_quicksort(arr, left, index-1)
	if index < right:
		book_quicksort(arr, index, right)
	return arr

def book_partition(arr, left, right):
	pivot = arr[(left + right)//2]
	# pivot = random.randint(left, right) CRASHES -- book sort algorithm does NOT WORK FOR RANDOM PIVOT
	def swap(i,j): arr[i],arr[j] = arr[j],arr[i]
	while left <= right:
		while arr[left] < pivot: left += 1
		while arr[right] > pivot: right -= 1
		if left <= right:
			swap(left, right)
			left += 1
			right -= 1
	return left

# identifies the first element in arr such that arr[result] <= target and arr[result+1] > target or result+1 is not in the array
def bin_search(arr,target):
	stack = [(0, len(arr))]
	while stack:
		low,high = stack.pop()
		if high-low <= 1:
			return low
		guess = (low + high)//2
		if arr[guess] <= target:
			low = guess
		elif arr[guess] > target:
			high = guess
		stack.append((low, high))

def test_sort(method, iterations=10, length=1000):
	for _ in range(iterations):
		a = [random.randint(-10*length,10*length) for i in range(length)]
		a = method(a)
		for i in range(len(a)-1):
			assert a[i] <= a[i+1], "ERROR %d not less than %d " % (a[i], a[i+1])

def test_quicksort():
	test_sort(quicksort)

import timeit
def compare_quicksorts():
	def test1(): test_sort(quicksort_a)
	def test2(): test_sort(quicksort_b)
	time1 = timeit.timeit(test1, number=1)
	time2 = timeit.timeit(test2, number=1)
	print("TIME WITH DOUBLE PARTITION: %f\nTIME WITH SINGLE PARTITION: %f" % (time1, time2))


def test_booksort():
	test_sort(book_quicksort)

def test_radix_sort():
	test_sort(radix_sort)

def test_merge_sort():
	test_sort(mergesort)

def test_bin_search():
	for _ in range(10):
		arr = sorted([random.randint(-1000,1000) for i in range(1000)])
		target = random.randint(-1200,1200)
		result = bin_search(arr, target)
		print(target)
		if target >= arr[-1]:
			assert result == len(arr) - 1, str(arr[result:result+2])
		elif target < arr[0]:
			assert result == 0, str(arr[result:result+2])
		else:
			assert arr[result] <= target and arr[result+1] > target, str(arr[result-1:result+2])


#### PROBLEMS #####
#### PROBLEMS #####
#### PROBLEMS #####
#### PROBLEMS #####

def sorted_merge(a,b):
	if not b: return a if a else []
	head = len(a) - 1
	i,j = head - len(b), len(b) - 1
	while j >= 0:
		if i >= 0 and a[i] > b[j]:
			a[head] = a[i]
			i -= 1
		else:
			a[head] = b[j]
			j -= 1
		head -= 1
	return a

def test_sorted_merge(len_a = 50, len_b = 10):
	a = sorted([random.randint(0,100) for i in range(len_a)])
	a.extend([None] * len_b)
	b = sorted([random.randint(0,150) for i in range(len_b)])
	a = sorted_merge(a,b)
	for i in range(len(a) - 1):
		assert a[i] <= a[i+1]
	print(a)

from functools import reduce
def group_anagrams(strings):
	if not strings:
		return []
	else:
		charmap = generate_charmap()
		anagrams = {}
		for word in strings:
			word_hash = anagram_hash(word, charmap)
			if word_hash in anagrams:
				anagrams[word_hash].append(word)
			else:
				anagrams[word_hash] = [word]
		return reduce(lambda x,y: x+y, [anagrams[word_hash] for word_hash in anagrams])

import math
def generate_primes(n):
	nums = list(range(1,n*10, 2))
	current_prime = 3
	highest_prime = int(math.sqrt(n*10))
	while current_prime < highest_prime:
		index = (current_prime*3)//2
		while index < len(nums):
			nums[index] = 0
			index += current_prime
		index = (current_prime//2) + 1
		while index < len(nums):
			if nums[index] != 0:
				current_prime = nums[index]
				break
			else:
				index += 1
	nums[0] = 2
	return list(filter(lambda x: x > 0, nums))[:n]

def generate_charmap():
	primes = generate_primes(26)
	return {chr(i):primes[i - ord('a')] for i in range(ord('a'),ord('z')+1)}

def anagram_hash(word, charmap=generate_charmap()):
	return sum(map(lambda c: charmap[c],word))

def make_word(max_length=10):
	return ''.join([chr(random.randint(ord('a'), ord('z'))) for c in range(random.randint(2, max_length))])

def test_group_anagrams(num_anagrams=10, max_length=10):
	strings = []
	for _ in range(num_anagrams):
		word = make_word(max_length)
		print(word)
		strings.append(word)
		for i in range(random.randint(0,max_length//2)):
			strings.append(''.join(shuffle(word)))
	strings = shuffle(strings)
	strings = group_anagrams(strings)
	print(strings)
	previous_anagrams = []
	current_hash = 0
	charmap = generate_charmap()
	for word in strings:
		if current_hash != anagram_hash(word, charmap):
			previous_anagrams.append(current_hash)
			current_hash = anagram_hash(word, charmap)
			assert current_hash not in previous_anagrams, "ERROR! Words not properly grouped"

def swap(arr,i,j):
	arr[i],arr[j] = arr[j],arr[i]

def shuffle(iterable):
	output = []
	for i in iterable:
		output.append(i)
		if len(output) > 1:
			swap(output,len(output)-1,random.randint(0,len(output)-1))
	return output

# supports recursive call to avoid advanced logic when low, guess, high are equal
# NEVERMIND, this WILL fail if there are LOTS of duplicates. The book example uses unique integers
def rotated_binary_search(arr, target, low = None, high = None):
	low, high = 0, len(arr) - 1
	while high-low > 1:
		guess = (low + high)//2
		if arr[guess] == target:
			return guess
		elif arr[low] == target or arr[high] == target:
			return low if arr[low] == target else high
		elif arr[guess] < target:
			if arr[high] >= target or (arr[high] < target and arr[high] < arr[guess]):
				low = guess
			else:
				high = guess
		elif arr[guess] > target:
			if arr[low] <= target or (arr[low] > target and arr[low] > arr[guess]):
				high = guess
			else:
				low = guess
	return -1

def rotate(arr, n):
	n %= len(arr)
	return arr[n:] + arr[:n]

class Listy:
	def __init__(self, lst):
		self._lst = lst

	def element_at(self,i):
		if i >= 0 and i < len(self._lst):
			return self._lst[i]
		else:
			return -1

def search_listy(listy, target):
	low = high = 0
	if listy.element_at(high) == -1:
		return -1
	else:
		high = 1
		while listy.element_at(high) != -1:
			high *= 2
		return binary_listy_search(listy, target, low, high)

def binary_listy_search(listy, target, low, high):
	while high - low >= 0:
		guess = (high + low)//2
		if listy.element_at(guess) == -1:
			high = guess - 1
		elif listy.element_at(guess) == target:
			return guess
		elif listy.element_at(guess) > target:
			high = guess - 1
		else:
			low = guess + 1
	return -1

## SORT BIG FILE ##

def sort_big_file(filename):
	if not filename:
		return []
	else:
		tree = BinarySearchTree()
		with open(filename) as file:
			for line in file:
				tree.insert(line.strip())
		return tree.sorted_list()

class Node:
	def __init__(self, value):
		self.value = value
		self.parent = self.left = self.right = None

	def __lt__(self, other):
		return self

class BinarySearchTree:
	def __init__(self):
		self._root = None

	def sorted_list(self):
		return self.__in_order_traversal(self._root)

	def __in_order_traversal(self, node):
		if node is None:
			return []
		else:
			return self.__in_order_traversal(node.left) + [node.value] + self.__in_order_traversal(node.right)

	def insert(self, value):
		target = self._root
		prev = None
		while target is not None:
			prev = target
			if value <= target.value:
				target = target.left
			else:
				target = target.right
		target = Node(value)
		if prev is not None:
			target.parent = prev
			if target.value <= prev.value:
				prev.left = target
			else:
				prev.right = target
		else:
			self._root = target

def generate_word_list(num_words=10000, max_length=20):
	return '\n'.join([make_word(max_length) for i in range(num_words)])

def make_word_list_file(num_words=10000, max_length=20, filename='test_words.txt'):
	word_list = generate_word_list()
	print(word_list)
	with open(filename, 'w') as file:
		file.write(word_list)
		print("SUCCESSFULLY WROTE WORD LIST")

## MISSING INT ##
def test_xor(limit=10000, tests=10):
	for __ in range(tests):
		nums = set()
		for _ in range(limit):
			nums.add(random.randint(0,limit*4)) # reduced change of collisions
		nums = list(nums)
		# print(nums)
		result = reduce(lambda x,y: x^y, nums)
		print(nums)
		print(result)
		assert (-1 * (~result) ) not in nums, nums[nums.index((-1 * (~result) ))]
		# assert result not in nums, nums[nums.index(result)]
		# print(bin(result))
		# print(~result)
		# print(bin(~result))

class BitVector:
	def __init__(self, length):
		self._vector = bytearray(length)
		self.length = length

	def set(self, bit_num):
		if self.__valid_bit(bit_num):
			self._vector[bit_num//8] |= (1 << bit_num % 8)

	def get(self, bit_num):
		if self.__valid_bit(bit_num):
			return (self._vector[bit_num//8] >> bit_num % 8) & 1

	def clear(self, bit_num):
		if self.__valid_bit(bit_num):
			self._vector[bit_num//8] &= ~(1 << bit_num % 8)

	def __valid_bit(self, bit_num):
		if bit_num < self.length:
			return True
		else:
			raise IndexError

	def __str__(self):
		return "0b" + ''.join([str(self.get(i)) for i in range(self.length-1,-1,-1)])

	def __repr__(self):
		return str(self)

import queue
class HuffmanTree:
	def __init__(self, training_data):
		self._training_data = training_data
		self._encoding_tree = None
		self._frequencies = None
		self.__calculate_frequencies()
		self.__build_encoding_tree()

	def __calculate_frequencies(self):
		self._frequencies = {}
		for c in self._training_data:
			if c in self._frequencies:
				self._frequencies[c] += 1
			else:
				self._frequencies[c] = 1
		print(self._frequencies)

	def __build_encoding_tree(self):
		if not self._frequencies:
			self.__calculate_frequencies()
		encoding_queue = queue.PriorityQueue()
		for c in self._frequencies:
			encoding_queue.put( (self._frequencies[c], Node([c])) )
		while not encoding_queue.empty():
			(freq1, node1) = encoding_queue.get()
			if encoding_queue.empty():
				self._encoding_tree = node1
			else:
				(freq2, node2) = encoding_queue.get()
				new_node = Node(node1.value + node2.value)
				new_node.left = node1
				new_node.right = node2
				node1.parent = new_node
				node2.parent = new_node
				encoding_queue.put((freq1 + freq2, new_node))

	def get_encoding_for_character(self, c):
		if not self._encoding_tree:
			self.__build_encoding_tree()
		node = self._encoding_tree
		encoding = ""
		while len(node.value) > 1:
			print(node.value)
			if c in node.left.value:
				encoding += "0"
				node = node.left
			else:
				encoding += "1"
				node = node.right
		return encoding
