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