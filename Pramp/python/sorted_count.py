"""
The "Word Count Engine" Problem

Implement a document scanning engine that receives a text document doc and returns a list of all unique words in it and their number of occurrences, sorted by the number of occurrences in descending order.

Example:
for doc: "practice makes perfect. get perfect by practice. just practice!"
the engine returns the list: { practice: 3, perfect: 2,  makes: 1, get: 1, by: 1, just: 1 }.

The engine should ignore punctuation and white-spaces.
Find the minimal runtime complexity and analyze it.
# 
#	doc = doc.lower()
# 	print(re.findall('[a-z\s]+',doc))
"""
# QUICK IMPLEMENTATION:
import re
import operator
def word_count(doc):
	punctuation_filter = re.compile('[^a-zA-Z]')
	words = map(lambda w: punctuation_filter.sub('',w).lower(),doc.split())
	counts = {}
	for word in words: counts[word] = counts.get(word,0) + 1
	return sorted(counts.items(),reverse=True,key=operator.itemgetter(1))
print(word_count('Practice makes perfect. get perfect by practice. just practice!'))

# from functools import reduce
# import operator
# import re

# def scan_document(doc):
# 	word_counts = count_words(doc)
# 	sorted_counts = sort_counts(word_counts)
# 	return sorted_counts

# def count_words(doc):
# 	punctuation_filter = re.compile('[^a-z]')

# 	def map_words(word): return {punctuation_filter.sub('',word.lower()):1} 
# 	def reduce_words(dict1, dict2):
# 		for word in dict2:
# 			if word in dict1:
# 				dict1[word] += dict2[word]
# 			else:
# 				dict1[word] = dict2[word]
# 		return dict1

# 	return reduce(reduce_words, map(map_words, doc.split()))

# def sort_counts(word_counts):
# 	return sorted(word_counts.items(), reverse = True, key=operator.itemgetter(1))

# def test_word_counts():
# 	doc = "practice makes perfect. get perfect by practice. just practice!"
# 	print(scan_document(doc))

# def print_counts(counts):
# 	print("\n".join(["%s:\t\t%d" % (count[0],count[1]) for count in counts]))

# import sys
# def run():
# 	doc = sys.argv[1]
# 	with open(doc) as file:
# 		result = scan_document(file.read())
# 		if len(result) > 200:
# 			print_counts(result[:200])
# 		else:
# 			print_counts(result)

# run()