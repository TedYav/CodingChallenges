import re
from functools import reduce

class WordCounter:
	def __init__(self, book):
		self._book = book
		self._word_filter = re.compile('[^A-Za-z]')
		self._word_map = None
		self.build_word_map()

	def build_word_map(self):
		if not self._word_map:
			def map_word(word):
				return {self._word_filter.sub('', word).lower(): 1}

			def reduce_words(words1, words2):
				for key in words2:
					if key in words1:
						words1[key] += words2[key]
					else:
						words1[key] = words2[key]
				return words1

			self._word_map = reduce(reduce_words, map(map_word, self._book.split()))

	def get_count(self, word):
		if not self._word_map:
			self.build_word_map()
		return self._word_map[word.lower()] if word.lower() in self._word_map else 0

def test():
	book = input().strip()
	print("Making word map.")
	word_counter = WordCounter2(book)
	print("Look up:")
	request = input().strip()
	while request != 'STOP':
		print('Looking up %s:\tResult: %d' % (request, word_counter.get_count(request)))
		print("Look up:")
		request = input().strip()

class WordCounter2:
	def __init__(self, text):
		self._text = text
		self._word_map = None
		self.build_word_map()

	def build_word_map(self):
		if not self._word_map:
			def reduce_words(words1, words2):
				for k in words2:
					words1[k] = words1.get(k,0) + words2[k]
				return words1
			regex_filter = re.compile('[^a-zA-Z]')
			self._word_map = map(lambda w: {regex_filter.sub('', w).lower(): 1}, self._text.split())
			self._word_map = reduce(reduce_words, self._word_map)

	def get_count(self, word):
		if not self._word_map:
			self.build_word_map()
		return self._word_map.get(word.lower(), 0)

def intersection(line1, line2):
	if not line1 or not line2:
		return None
	else:
		line1.sort()
		line2.sort()
		intersect = None
		if slope(line1) != slope(line2):
			point = find_intersection(line1, line2)
			if point_is_on_line(point, line1) and point_is_on_line(point, line2):
				intersect = point
		else:
			for point in line2:
				if point_is_on_line(point, line1):
					intersect = point
		return intersect

def slope(line):
	return (line[1][1] - line[0][1])/(line[1][0] - line[0][0])

def point_is_on_line(point, line):
	if point[1] - line[0][1] == slope(line) * (point[0] - line[0][0]):
		if point[0] >= line[0][0] and point[0] <= line[1][0]:
			return True
	return False

def find_intersection(line1, line2):
	x1,y1 = line1[0]
	x2,y2 = line2[0]
	m1,m2 = slope(line1), slope(line2)
	x = (y2 + (m1*x1) - (m2*x2) - y1)/(m1-m2)
	y = (m2*x) - (m2*x2) + y2
	return (x,y)

def factorial(n):
	return reduce(lambda x,y: x*y, range(n,1,-1))

def num_trailing_zeros(n):
	count = 0
	while n%10 == 0:
		count += 1
		n //= 10
	return count

def factorial_zeroes(n):
	pow = 1
	zeroes = 0
	while n//(5**pow) > 0:
		zeroes += n//(5**pow)
		pow += 1
	return zeroes

def smallest_diff(arr1,arr2):
	if not arr1 or not arr2:
		return None
	else:
		min_diff = max(arr1[-1],arr2[-1]) - min(arr1[0], arr2[0]) + 1
		min_indices = (-1,-1)
		arr1.sort()
		arr2.sort()
		i = j = 0
		while i<len(arr1) and j<len(arr2):
			current_diff = abs(arr1[i] - arr2[j])
			if current_diff < min_diff:
				min_diff = current_diff
				min_indices = (i,j)
			if arr1[i] < arr2[j]:
				i += 1
			elif arr1[i] > arr2[j]:
				j += 1
			else:
				break
		return (min_diff, min_indices)
			
### ENGLISH NUMBER (#8) ###
def english_int(num):
	output = []
	negative = ""
	if num is not None:
		if num == 0:
			output = ["zero"]
		else:
			negative = "negative " if num < 0 else ""
			if negative: num *= -1
			current_block = 0
			while num//(1000**current_block) > 0:
				current_digits = num//(1000**current_block) % 1000
				prefix = block_prefix(current_digits)
				if prefix:
					output.append(block_prefix(current_digits) + block_suffix(current_block))
				current_block += 1
	return negative + ", ".join(output[::-1])

def block_prefix(num):
	if num == 0: 
		return ""
	else:
		output = []
		teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
		one_to_ten = ["","one","two","three","four","five","six","seven","eight","nine"]
		multiples_of_ten = ["","ten","twenty", "thirty","forty","fifty","sixty","seventy","eighty","ninety"]
		hundred = "hundred"
		
		hundreds_place = num//100
		if hundreds_place > 0:
			output.append(one_to_ten[hundreds_place] + " " + hundred)

		tens_place = (num%100) // 10
		ones_place = num%10
		if tens_place > 0 and tens_place != 1:
			output.append(multiples_of_ten[tens_place])
		
		if tens_place == 1:
			output.append(teens[ones_place])
		elif ones_place > 0:	
			output.append(one_to_ten[ones_place])
		
		return " ".join(output)

def block_suffix(block_number):
	blocks = ["", " thousand", " million", " billion", " trillion", " quadrillion", " quintillion"]
	return blocks[block_number] if block_number < len(blocks) else "fuckload"

##### OPERATORS WITH ONLY ADD #####

def negate(num):
	delta = -1 if num > 0 else 1
	negated_num = 0
	while num + negated_num != 0:
		next_sum = num + negated_num + delta
		if num > 0 and next_sum < 0:
			delta = -1
		elif num < 0 and next_sum > 0:
			delta = 1
		negated_num += delta
		delta += delta
	return negated_num

def subtract(a,b):
	return a + negate(b)

def different_signs(a,b):
	return (a < 0 or b < 0) and not (a<0 and b<0)

def abss(a):
	return a if a > 0 else negate(a)

def multiply(a,b):
	negative = different_signs(a,b)
	a,b = abss(a),abss(b)
	a,b = b,a if b>a else a,b
	sum = 0
	while b>0:
		sub += a
		b = subtract(b,1)
	return sum if not negative else negate(sum)

def divide(a,b):
	negative = different_signs(a,b)
	a,b = abss(a),abss(b)
	quotient = 0
	product = b
	while product <= a:
		product += b
		quotient += 1
	return quotient if not negative else negate(quotient)

##### LIVING PERSONS #####

import heapq

class Person:
	def __init__(self,birth,death):
		self.birth = birth
		self.death = death

	def __lt__(self, other):
		return self.birth < other.birth

	def __str__(self):
		return "\nBirth: %d Death: %d" % (self.birth, self.death)
	def __repr__(self):
		return str(self)

def living_persons_suboptimal(people, years=[1900,2000]):
	people.sort()
	people_alive = 0
	max_alive = 0
	max_year = 0
	current_year = years[0]
	people_queue = []
	for person in people:
		while person.birth > current_year: current_year += 1
		while people_queue and people_queue[0] < current_year: 
			heapq.heappop(people_queue)
			people_alive -= 1
		people_alive += 1
		heapq.heappush(people_queue, person.death)
		if people_alive > max_alive:
			max_alive = people_alive
			max_year = current_year
	return (max_alive, max_year)

def living_persons_optimal(people, years=[1900,2000]):
	year_deltas = [0 for i in range(years[0],years[1]+1)]
	for person in people:
		year_deltas[person.birth - years[0]] += 1
		if person.death < years[1]: year_deltas[person.death - years[0] + 1] -= 1
	max_population = max_year = 0
	current_population = 0
	for year in range(len(year_deltas)):
		current_population += year_deltas[year]
		if current_population > max_population:
			max_population = current_population
			max_year = year
	return (max_population, max_year + years[0])

import random
def test_living_persons(n=500, start=1900, end=2000):
	people = []
	for i in range(n):
		birth = random.randint(start,end)
		death = random.randint(birth,end)
		people.append(Person(birth,death))
	return people

##### DIVING BOARD #####
def possible_lengths(k, l, s):
	if k == 0:
		return 1
	elif min([k,l,s]) <= 0:
		return 0
	else:
		(l,s) = (s,l) if s>l else (l,s)
		return list(range(k*s,k*l+1,l-s))

##### XML ENCODING #####
from functools import reduce
class Element:
	def __init__(self,element_type,value="",attributes={},children=[]):
		self.element_type = element_type
		self.value = value
		self.attributes = attributes
		self.children = children

def encode(elements,mapping):
	if not elements or not mapping:
		raise ValueError('Invalid input')
	else:
		return reduce(lambda x,y: x+" " + y, map(lambda e: xml_encode(e,mapping), elements))

def xml_encode(element,mapping):
	if not element.element_type in mapping:
		raise ValueError('No defined mapping for element type %s' %element.element_type)
	else:
		output = [mapping[element.element_type]]
		for attribute in element.attributes:
			if attribute not in mapping:
				raise ValueError('No defined mapping for attribute type %s' % attribute)
			else:
				output.append(mapping[attribute])
				output.append(element.attributes[attribute])
		output.append(0)
		if element.value:
			output.append(element.value)
			output.append(0)
		output.extend(map(lambda e: xml_encode(e,mapping), element.children))
		if element.children: output.append(0)
		return reduce(lambda x,y: str(x) + " " + str(y), output)

def test_xml_encode():
	child = Element("person", value="Some Message", attributes={"firstName":"Gayle"})
	parent = Element("family", attributes={"lastName": "McDowell", "state":"CA"}, children=[child])
	mapping = {"family":1,"person":2,"firstName":3,"lastName":4,"state":5}
	print(encode([parent],mapping))

##### BISECT SQUARE #####
class Coordinate:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(%.2f,%.2f)" % (self.x, self.y)

	def __repr__(self):
		return str(self)

class Square:
	def __init__(self, size, left_corner):
		self.coordinates = [left_corner, \
							Coordinate(left_corner.x + size, left_corner.y),\
							Coordinate(left_corner.x, left_corner.y + size),\
							Coordinate(left_corner.x + size, left_corner.y + size)]

	def center(self):
		return Coordinate(((self.coordinates[3].x - self.coordinates[0].x)/2) + self.coordinates[0].x, \
						((self.coordinates[3].y - self.coordinates[0].y)/2) + self.coordinates[0].y) 

import sys
import random
class LineUtility:
	def __init__(self, line):
		self.line = line

	def get_random_point_on_line(self, x_range=[-1000,1000]):
		x = random.random() * (x_range[1] - x_range[0]) + x_range[0]
		y = self.line.coordinate1.y + (x - self.line.coordinate1.x)*self.line.slope()
		return Coordinate(x,y)

class Line:
	def __init__(self, coordinate1, coordinate2):
		self.coordinate1 = coordinate1
		self.coordinate2 = coordinate2
		self.__epsilon = 0.01

	def slope(self):
		return (self.coordinate2.y - self.coordinate1.y)/(self.coordinate2.x - self.coordinate1.x) if self.coordinate1.x != self.coordinate2.x else sys.maxsize

	def point_is_on_line(self, coordinate):
		return abs((coordinate.y - self.coordinate1.y) - ((coordinate.x - self.coordinate1.x)*self.slope())) <= self.__epsilon

	def __str__(self):
		return "y - %.2f = (x - %.2f)*%.2f" % (self.coordinate1.y, self.coordinate1.x, self.slope())

	def __repr__(self):
		return str(self)

	def __hash__(self):
		intercept = round((self.coordinate1.y - (self.coordinate1.x * self.slope())),3)
		slope = round(self.slope(),3)
		return hash((slope, intercept))

	# epsilon = tolerance for comparison
	def __eq__(self, other):
		conditions = []
		conditions.append(abs(self.slope()-other.slope())<=self.__epsilon)
		conditions.append(self.point_is_on_line(other.coordinate1))
		conditions.append(self.point_is_on_line(other.coordinate2))
		return all(conditions)

def bisect_squares(square1, square2):
	if not square1 or not square2:
		return None
	else:
		print(Line(square1.center(), square2.center()))

def test_bisect_squares():
	square1 = Square(5, Coordinate(0,0))
	square2 = Square(5, Coordinate(6,0))
	bisect_squares(square1, square2)

	square1 = Square(3, Coordinate(5,25))
	square2 = Square(34, Coordinate(49,0))
	bisect_squares(square1, square2)

"""

BEST LINE: given 2d grid with points, find line that intersects most points ("passes"?? wtf.)
STRATEGY:
	1. Calculate all pairs of points and slopes, O(n^2) -- return most common line segment

"""

def best_line(points):
	if not points:
		return None
	else:
		lines = {}
		max_line = None
		max_value = 0
		for i in range(len(points)-1):
			for j in range(i+1, len(points)):
				temp_line = Line(points[i],points[j])
				if temp_line in lines:
					lines[temp_line] += 1
				else:
					lines[temp_line] = 1
				if lines[temp_line] > max_value:
					max_value = lines[temp_line]
					max_line = temp_line
		return (max_line, max_value)

def test_best_line(num_points=500, p=0.35, x_range=[-10000,10000], y_range=[-10000,10000]):
	points = []
	while len(points) < num_points:
		point1 = Coordinate(rand_between(*x_range), rand_between(*y_range))
		point2 = Coordinate(rand_between(*x_range), rand_between(*y_range))
		points.append(point1)
		points.append(point2)
		point_generator = LineUtility(Line(point1,point2))
		while random.random() >= 1-p:
			points.append(point_generator.get_random_point_on_line())
	print(best_line(points))

def rand_between(a,b):
	return random.random() * (b - a) + a

"""

	MASTERMIND:
		PICK from four colors: R,G,Y,B
		Each move, make a guess:
			HIT: correct color, correct slot
			PSEUDO-HIT: correct color, incorrect slot
			HIT CAN NEVER BE PSEUDO HIT
			e.g.: Solution: RGBY, GUESS GGRR, one hit (G in slot 2), one pseudo hit, R in slot 3 or 4
		Return # of hits and pseudo hits, given guess and solution

		RGBY === BY
		GGRR === GR

	NAIVE: iterate, remove and count hits from both arrays, compare again, for each element in second array if in first, remove, count one pseudo hit
	BETTER: rather than removing from array (O(n)), just set to None

"""

def score_solution(guess,solution):
	if not guess or not solution or len(guess) != len(solution):
		return None
	else:
		hits = 0
		pseudo_hits = 0
		for i in range(len(guess)):
			if guess[i] == solution[i]:
				hits += 1
				solution[i] = None
				guess[i] = None
		for i in range(len(guess)):
			if guess[i] and guess[i] in solution:
				pseudo_hits += 1
				solution[solution.index(guess[i])] = None
		return (hits, pseudo_hits)

def test_score_solution():
	solution = ['R','G','B','Y']
	guess = ['G','G','R','R']
	assert score_solution(guess, solution) == (1,1)
	print(score_solution(guess, solution))

	solution = ['G','G','G','G']
	guess = ['G','R','G','R']
	assert score_solution(guess, solution) == (2,0)
	print(score_solution(guess, solution))

"""

	SUBSORT:
		Given array, find m, n such that sorting array[m:n+1] means that array is sorted
		Find m,n s.t. there is no values possible with a lesser difference (minimum difference to keep array sorted)

		[1,2,4,7,10,11,7,12,6,7,16,18,19]

		any array a can be decomposed into three arrays of lenght >= 0:
			a = a + b + c
				a and c are sorted, b is not
				SO, if I can find index i and j s.t. i = end(a), j = beginning(c)
				AND I can find min, max in b
				THEN I can use binary search in a and c to find the indices where I would need to sort

				LET sort_min = min(b)
				LET sort_max = max(b)

				m = first index in a s.t. a[m] > sort_min
				n = last index in c s.t. c[n] < sort_max

				NEED binary search that returns first element >= value

"""

def sub_sort(arr):
	if not arr:
		return None
	else:
		i = 1
		j = len(arr) - 2
		found_i = False
		found_j = False
		while i <= j and not (found_i and found_j):
			if not found_i:
				if arr[i] < arr[i-1]:
					found_i = True
					i = i-1
				else:
					i += 1
			
			if not found_j:
				if arr[j] > arr[j+1]:
					found_j = True
					j = j+1
				else:
					j -= 1
		if i > j:
			# array is sorted already
			return (0,0)
		else:
			sort_min = min(arr[i+1: j])
			sort_max = max(arr[i+1: j])
			m = binary_search(arr[:i+1],sort_min + 1)
			n = binary_search(arr[j:],sort_max - 1) + j
			while arr[m] < sort_min or arr[m] == arr[m+1]: m += 1
			return (m,n)

def binary_search(arr,target):
	low = 0
	high = len(arr) - 1
	while high - low >= 0:
		mid = (low + high)//2
		if arr[mid] == target:
			return mid
		elif arr[mid] > target:
			high = mid - 1
		elif arr[mid] < target:
			low = mid + 1
	return low if arr[low] < target else high


"""

	CONTIGUOUS SEQUENCE:
		Given array, positive and negative, find contiguous sequence with largest sum
		NAIVE: O(n^2) -- check every start and end point
		BETTER: since I'm starting with 0 at any point, any time sum drops below 0 I move onto next sum, skip negative numbers
		(If all negative return 0)

"""

def maximum_subsequence(arr):
	max_sum = 0
	if arr:
		current_sum = 0
		for e in arr:
			current_sum += e
			if current_sum < 0: current_sum = 0
			if current_sum > max_sum: max_sum = current_sum
	return max_sum

"""

	PATTERN MATCHING:
		given a pattern string:
			ex: ababab
			determine if provided string matches patterns

		BRUTE FORCE: all possible values of A and B
			This is O(n^4) -- because O(n^2) substrings
			NOW many are mutually exclusive. How can we do better?

		ANY string will match: a, b, ab, ba, ""
		aaa or bbb -- string must be divisible by 3 (or n == number of pattern elements)
		ababa, string s can be decomposed into n_a strings lenght l_a, n_b strings lenght n_b
			let's call that x == len(a), y == len(b), n == num occurences of a, m = # occurences b
			SO: len(s) = n*x + m*y
			ALSO: x >= 1, y >= 1

		STRATEGY:
			MAX X: (len(s) - m)//n
			For x in range(1,MAX_X)
			Assign x = 1, my = (len(s) - n)
				IF (len(s) - n)%m != 0
					Continue
				else:
					check if string matches pattern
			TO CHECK:
				If first pattern is a: read first x characters, else if b, read first y
					STORE
				Compare future patterns against these, as soon as mismatch, continue
				If end of string reached, return True
			If loop completes, return False

"""

def pattern_matches_string(s, pattern):
	if s is None or pattern is None or len(list(filter(lambda x: x=='a' or x=='b',pattern))) != len(pattern):
		return False
	elif pattern in ["", "a", "b", "ab", "ba"]:
		return True
	else:
		count_a = pattern.count('a')
		count_b = pattern.count('b')
		if count_a == 0 or count_b == 0:
			return is_repeated_string(s, (count_a if count_a > 0 else count_b))
		else:
			maxlen_a = (len(s) - count_b)//count_a
			for len_a in range(1,maxlen_a + 1):
				total_b = len(s) - (count_a * len_a)
				if total_b % count_b != 0: continue
				len_b = total_b//count_b
				if verify_pattern(s, pattern, len_a, len_b): return True
			return False

def verify_pattern(s, pattern, len_a, len_b):
	patterns = {'a':'', 'b':''}
	pattern_index = 0
	current_pattern = pattern[pattern_index]
	pattern_position = 0
	for i in range(len(s)):
		current_pattern = pattern[pattern_index]
		
		if not validate_character(s[i], current_pattern, pattern_position, patterns, len_a, len_b): 
			return False
		
		pattern_position += 1
		
		if should_switch_pattern(current_pattern, pattern_position, len_a, len_b):
			pattern_index += 1
			pattern_position = 0

		if i==len(s) - 1:
			return True

def validate_character(current_char, current_pattern, pattern_position, patterns, len_a, len_b):
	length = len_a if current_pattern == 'a' else len_b
	if len(patterns[current_pattern] < length):
		patterns[current_pattern] += current_char
		return True
	else:
		return current_char == patterns[current_pattern][pattern_position]		

def should_switch_pattern(current_pattern, pattern_position, len_a, len_b):
	conditions = []
	conditions.append(current_pattern == 'a' and pattern_position == len_a)
	conditions.append(current_pattern == 'b' and pattern_position == len_b)
	return any(conditions)

def is_repeated_string(s, count):
	chunks = []
	if len(s) % count != 0: return False
	else:
		chunk_size = len(s)//count
		for i in range(count):
			chunks.append(s[i*chunk_size:(i+1)*chunk_size])
		return len(set(chunks)) == 1

"""

	POND SIZES:
		input: matrix, with plot of land representing height above sea level
		ASSUME: 0 == pond, so no negative values (or, at least, negative values don't count as water)

	SIMPLE SOLUTION:
		Two Functions: Scan --> O(n*m), Measure_Pond (recursive) --> O(size of pond)
		Overall O(n*m) + O(sum(pond sizes)) == O(n*m)

		02323290
		03920000

"""

def pond_sizes(land):
	if not land:
		return None
	else:
		output = []
		width = len(land[0])
		height = len(land)
		for row in range(height):
			for col in range(width):
				if land[row][col] == 0:
					output.append(measure_pond(land, row, col))
		print(", ".join(map(str,output)))
		return output

def measure_pond(land, row, col):
	stack = [(row,col)]
	size = 0
	while stack:
		row,col = stack.pop()
		if land[row][col] == 0:
			land[row][col] = -1
			size += 1
			next_squares = [(row + i, col + j) for i in range(-1,2,1) for j in range(-1,2,1)]
			next_squares = list(filter(lambda t: is_pond(land,t[0],t[1]), next_squares))
			stack.extend(next_squares)
	return size

def is_pond(land,row,col):
	conditions = []
	conditions.append(row >= 0)
	conditions.append(col >= 0)
	conditions.append(row < len(land))
	conditions.append(col < len(land[0]))
	return (land[row][col] == 0) if all(conditions) else False

def test_pond_sizes(n=1000,m=1000):
	land = [[0,2,1,0],[0,1,0,1],[1,1,0,1],[0,1,0,1]]
	pond_sizes(land)

	land = [[random.randint(-1000,1000) for i in range(n)] for j in range(m)]
	land = list(map(lambda row: list(map(lambda c: 0 if c < 0 else c, row)), land))
	total_pond = sum(map(lambda row: row.count(0), land))
	print(land)
	print(total_pond)
	result = pond_sizes(land)
	print(sum(result))
	assert sum(result) == total_pond

"""

	T9:

	AWFUL: array of tuples [(xxxx, word),(yyyy,word2)]
	BAD: dictionary {xxxx:word1,word2, yyyy:word3,word4} (FASTEST, but what if we have a lot of words?)
	BEST: tree: nodes have key and values
		root: key 0
		key: 0-9
		children: 0-9
		words: words that end at this node

"""
class T9Node:
	def __init__(self, key=0):
		self.key = key
		self.words = []
		self.children = [None for i in range(10)]

class T9Tree:
	def __init__(self, words=[]):
		self.__root = T9Node()
		self.__mapping = self.make_mapping()
		for word in words:
			self.add_word(word)

	def lookup_word(self, code):
		node = self.__root
		code = str(code)
		for digit in code:
			node = node.children[int(digit)]
			if node is None: return []
		return node.words

	def make_mapping(self):
		nums = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
		mapping = {chr(c):nums[c - ord('a')] for c in range(ord('a'), ord('z') + 1)}
		print(mapping)
		return mapping

	def word_to_code(self, word):
		code = 0
		word = word.lower()
		for c in word:
			code *= 10
			code += self.__mapping[c]
		return code

	def add_word(self, word):
		node = self.__root
		word = word.lower()
		for c in word:
			digit = self.__mapping[c]
			if node.children[digit] is None:
				node.children[digit] = T9Node(key=digit)
			node = node.children[digit]
		node.words.append(word)

def test_T9_tree():
	words = ['apple', 'Orange', 'banana', 'pear', 'girl', 'python', 'Google', 'tree', 'used']
	tree = T9Tree(words)
	print(words)
	codes = list(map(lambda word: tree.word_to_code(word), words))
	print(codes)
	for code in codes:
		print("WORD FOR CODE: %d IS: %s" % (code, tree.lookup_word(code)))


"""

	SUM SWAP
	Input: two arrays of integers
	Goal: find value in each array such that swapping them means sum(a1) == sum(a2)

		SPECIAL CASES:
			Bad Input: None
			Sums are the Same: Need to find number contained in both arrays
			Difference is Odd: Can't Do Operation

		WAYS TO SOLVE:
			NAIVE: Calculate array sums, go through array 1, for each value look through array 2 for complement
				O(nm) -- probably best we can do with O(1) space complexity
			BETTER: Go through array 1 and array 2 to calculate sums, store values in hashmaps at same time
				THEN: iterate through hashmap of a looking for complementary value in hashmap for b
				O(n + m) -- iterate through each array once and iterate through hashmaps once

				USE SET instead -- instead of adding to dict as I go, add all to set
					Time complexities of set are similar as implementations are similar
					BENEFIT: no duplicates -- less iteration
					LIST: O(n) to check if element in list -- no good

	COMPLEMENTARY NUMBER:
		If sum(s1) = a and sum(s2) = b:
			Need to find numbers c and d s.t. a - c + d = b - d + c
				ONCE c is chosen from set1, then: 2d = b - a + 2c
					==> d = (b - a + 2c)/2
"""


def sum_swap(arr1, arr2):
	result = []

	if not arr1 or not arr2: return result
	
	sum1, sum2 = sum(arr1), sum(arr2)
	if (sum1 - sum2)%2 == 1: return result

	set1, set2 = set(arr1), set(arr2)
	if sum1 == sum2:
		values = set1&set2
		if len(values) > 0:
			result = list(values)[0]
			result = [result, result]
	else:
		for value in set1:
			complement = (sum2 - sum1 + (2*value))//2
			if complement in set2:
				result = [value, complement]
				break

	return result

def test_sum_swap():
	print(sum_swap([4,1,2,1,1,2], [3,6,3,3]))

"""

	Langton's Ant

		GIVEN: k == number of moves,
		OUTPUT: final grid

		STRATEGY:
			ASSUME starting on white square
			create hashmap: store coordinates (x,y):color
			start at 0,0: color initially white
			change to black, add to hashmap
			have formula for non-visited squares

			keep track of min_x, min_y, max_x, max_y, direction (1,2,3,4) == (right, down, left, up)

			render grid at end

			formula for square: (0,0) is white
			FOR ALL EVEN X VALUES (0,2,4....), EVEN Y == White, ODD Y == Black
			FOR ALL ODD  X VALUES (-1,1,3...), EVEN Y == Black, ODD Y == White

			Rendering grid, remember rows are y values, columns are x


	0
270	   90
   180


"""

class Direction:
	def __init__(self):
		self.direction = 90

	def turn_right(self):
		self.direction += 90
		self.direction %= 360

	def turn_left(self):
		self.direction -= 90
		self.direction %= 360

	def get_next_square(self, coordinate):
		mappings = {0: (0,1), 90: (1,0), 180: (0,-1), 270: (-1, 0)}
		delta_x, delta_y = mappings[self.direction]
		return (coordinate[0] + delta_x, coordinate[1] + delta_y)

def simulate_moves(k):
	if k <= 0: return render_grid()

	x_bounds = [0,0]
	y_bounds = [0,0]
	position = (0,0)
	visited = {}
	direction = Direction()
	for i in range(k):
		current_color = visited[position] if position in visited else get_color(position)
		if current_color == 'W':
			visited[position] = 'B'
			direction.turn_right()
		else:
			visited[position] = 'W'
			direction.turn_left()
		position = direction.get_next_square(position)
		update_bounds(x_bounds, position[0])
		update_bounds(y_bounds, position[1])
	render_grid(visited, x_bounds, y_bounds)

def update_bounds(bounds, coordinate):
	if coordinate < bounds[0]:
		bounds[0] = coordinate
	elif coordinate > bounds[1]:
		bounds[1] = coordinate

def get_color(position):
	if position[0] % 2 == 0:
		return 'W' if position[1] % 2 == 0 else 'B'
	else:
		return 'B' if position[1] % 2 == 0 else 'W' 

# if offset for x and y is 5, then grid[0][0] really refers to (-5, -5)

def render_grid(visited = {}, x_bounds = [0,0], y_bounds=[0,0]):
	x_offset = abs(x_bounds[0])
	y_offset = abs(y_bounds[0])
	grid = []

	# render rows top to bottom
	for y in range(y_bounds[1], y_bounds[0] - 1, -1):
		row = []
		for x in range(x_bounds[0], x_bounds[1] + 1):
			coordinate = (x,y)
			if coordinate in visited:
				row.append(visited[coordinate])
			else:
				row.append(get_color(coordinate))
		grid.append(row)

	print("\n".join(list(map(lambda row: "".join(row), grid))))

def test_ant(k=5):
	simulate_moves(k)

"""

Rand(7) from Rand(5)

5 and 7 are relatively prime (GCD(5,7) == 1)
BUT -- if I can map some numbers using rand5 to a range where there is ONLY ONE way to make each number
THEN I can return a value, so long as it is evenly divisible by 7 as well

NOW-- If I do 5*(0-4) + (0-4) I have one way to get each # from 0 to 24
	Thus, Probability of each is 1/24th

BUT-- If I cut off 22-24, then I have an equal probability of getting a remaining number. 1/21 == (1/7)/3
If I mod this with 7 I'll get a number 

"""

def rand5():
	return random.randint(0,4)

def rand7_wrand5():
	while True:
		num = 5*rand5() + rand5()
		if num < 21:
			return num%7

def test_rand7(iterations=1000):
	test_rand(iterations, 7, rand7_wrand5)

def rand3():
	return random.randint(0,2)

def rand5_wrand3():
	while True:
		num = 3*rand3() + rand3()
		if num < 5: return num%5

def rand13_wrand3():
	def rand9(): return 3*rand3() + rand3()
	while True:
		num = 9*rand9() + rand9()
		if num < 78: return num%13

### DEVELOP RAND_X_W_Y FUNCTION

def rand_x_with_y(base1, base2):
	if base1 <= 1 or base2 <= 1: return None
	else:
		def rand(): return random.randint(0,base1-1)
		multipliers = [1]
		while multipliers[-1]*(base1-1) < base2:
			multipliers.append(multipliers[-1] * base1)
		target = ((multipliers[-1]*base1)//base2)*base2
		while True:
			num = sum([multiplier*rand() for multiplier in multipliers])
			if num < target:
				return num % base2

def test_rand_x_with_y(base1, base2, iterations=10000):
	def test_func(): return rand_x_with_y(base1, base2)
	test_rand(iterations, base2, test_func)

def test_rand5(iterations=1000):
	test_rand(iterations, 5, rand5_wrand3)

def test_rand13(iterations=1000):
	test_rand(iterations, 13, rand13_wrand3)

def test_rand(iterations, limit, func):
	print("EXPECTED COUNTS: %.2f%%" % (100/limit))
	counts = {k:0 for k in range(limit)}
	for i in range(iterations):
		counts[func()] += 1
	print({k:v/(iterations/100) for k,v in counts.items()})


"""

	PAIRS WITH SUM:
		INPUT: array with integers, target value
		OUTPUT: all pairs that sum to the target

	STRATEGIES:
		1. Naive -- just try all pairs. O(n^2)
		2. Better -- sort the array O(nlogn), start at beginning and end, move to middle O(n): overall O(nlogn)
		3. Best -- put all elements into hashmap along with counts, iterate over keys, note number of pairs that sum to target. O(n) + O(number of pairs)

"""

def pairs_with_sum(arr, target):
	if not arr: return []
	else:
		counts = {}
		for num in arr:
			if num in counts:
				counts[num] += 1
			else:
				counts[num] = 1
		pairs = []
		for num in counts:
			complement = target - num
			if complement in counts:
				if num != complement:
					for i in range(counts[num]):
						for j in range(counts[complement]):
							pairs.append((num, complement))
				else:
					for i in range(counts[num]):
						for j in range(i+1, counts[num]):
							pairs.append((num, num))
				counts[num] = 0
				counts[complement] = 0
		return pairs

def test_pairs_with_sum(n=1000, p=0.25):
	arr = [random.randint(-n,n) for i in range(n)]
	target = random.randint(-n,n)
	for i in range(1,n):
		if random.random() < p:
			arr[random.randint(0,i-1)] = target - arr[i]
	pairs = pairs_with_sum(arr, target)
	print(pairs)
	assert all([pair[0] + pair[1] == target for pair in pairs])

"""

	LRU Cache

	Goal: map from k to value, store max size
	When we reach max size, evict LRU item

	NAIVE: Add all elements to a dictionary as key: (value, accesstime), increment accesstime upon access
		When cache is full, scan over all, delete lowest access
		Problem: eviction takes O(n) time --> slow :(

	BETTER: Store items in dictionary, create an item class that stores access time
			Store items also in min_queue with first access time. Pop items from min queue
				If access time in queue == access time on item, then we delete it from the cache, else pop next

			Good: O(log n) time to add to queue. Problem is that repeated accesses all take O(logn) time.

	BEST: store items in dictionary AND in double linked list. When item is accessed, move it to tail.
		When queue full, delete head.

		O(1) deletions, finds (tail and head), appends
		Dictionary storage makes access random and O(1) as well

"""

class CacheNode:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
		self.prev = None

	def __str__(self):
		return str(self.value)

	def __repr__(self):
		return str(self)

class LRUCache:
	def __init__(self, max_size):
		if max_size <= 0:
			raise ValueError("Max Size must be at least 1")
		self.max_size = max_size
		self.size = 0
		self.__head = None
		self.__tail = None
		self.__key_map = {}

	def add(self, key, value):
		node = CacheNode(key, value)
		self.__key_map[key] = node
		if self.__head is None:
			self.__head = node
			self.__tail = node
		else:
			node.next = self.__tail
			node.next.prev = node
			self.__tail = node
		self.size += 1
		if self.size > self.max_size:
			self.__evict_oldest()

	def get(self, key):
		if key not in self.__key_map: raise IndexError()
		node = self.__key_map[key]
		if self.__head == node:
			self.__head = self.__head.prev
		if node.next is not None:
			node.next.prev = node.prev
		if node.prev is not None:
			node.prev.next = node.next
		node.next = self.__tail
		node.prev = None
		self.__tail = node
		return node.value

	def __evict_oldest(self):
		node = self.__head
		del self.__key_map[node.key]
		self.__head = self.__head.prev
		if self.__head is not None:
			self.__head.next = None
		else:
			self.__tail = None

	def __str__(self):
		return str(self.__key_map)

	def __repr__(self):
		return str(self)


"""

	CALCULATOR:
		input: arithmetic expression, positive integers without parentheses (+, -, *, /)
		NAIVE: left to right -- problem: wrong answer
		BETTER: left to right, first do multiplication and division, then addition and subtraction. Requires two passes
		BEST: build tree using operation class --> build tree then execute

	In reality, I might use inheritance for this. In this case I'll use one class and if statements

	ACTUALLY: it's not recursive. Just do left to right, mult and div first, add subtract second.

"""

def evaluate_expression(expr):
	if not expr: return 0
	else:
		expr = [int(i) if i not in ['-','+','/','*'] else i for i in expr]
		expr = evaluate_mult_divide(expr)
		expr = evaluate_add_subtract(expr)
		return expr[0]

def evaluate_mult_divide(expr):
	output = []
	i = 0
	while i < len(expr):
		if expr[i] == '*':
			output[-1] *= expr[i+1]
			i += 2
		elif expr[i] == '/':
			output[-1] //= expr[i+1]
			i += 2
		else:
			output.append(expr[i])
			i += 1
	return output

def evaluate_add_subtract(expr):
	output = []
	i = 0
	while i < len(expr):
		if expr[i] == '+':
			output[-1] += expr[i+1]
			i += 2
		elif expr[i] == '-':
			output[-1] -= expr[i-1]
			i += 2
		else:
			output.append(expr[i])
			i += 1
	return output


