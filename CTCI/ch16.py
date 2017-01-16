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

