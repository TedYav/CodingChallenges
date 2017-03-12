"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".
Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".
Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
How big is my character set? Lower case? 26 letters?
Solution 1:
Turn each word into set O(# letters)
Examine all pairs O(n^2 * O(1)) → O(26) for each set intersection.

Realistically here: cannot do better than O(n^2) because we must look at all the pairs.

Slight optimization: memoize the sets as we go so that we don’t calculate size of set if we don’t need to. Doesn’t reduce asymptotic complexity. (Only helps if we have ton of very large words and it’s likely we’re going to find the pair early on and they’re sorted by length)

Could sort by word length: will not reduce asymptotic complexity. Likely increase total running time (don’t have time for complex analysis right now)

POSSIBLE Solution 2:
Make dictionary of letters -> words those letters appear in. Intersect letter sets to see if words are disjoint in some manner.
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
	{
		‘a’: {0,1,3,5}
		'b': {0,1,3,5}
		'c': {0,5}
		'd': {5}
		'e': {5}
...
}

	Alternative: keep list of words letter DOESN'T appear in. Go from longest word down checking letter by letter. 

	Going to code solution 1 because this is taking too long.

"""

# Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]

def build_letter_sets(words):
letter_sets = []
for word in words:    	# letter_sets = [{'abcw'}, {'abz'}, {'fo'}, {'abr'}, {'fntx'}, {'abcdef'}]
letter_sets.append(set(word))
	return letter_sets

"""

|	i	|	j	|	words[i]	| 	words[j]	| 	len(intersection)	|	max_product	|
|	0	|	1	|	abcw		|	abz		|	2				|	0			|
|	0	|	2	|	abcw		|	fo		|	0				|	8			|
|	0	|	3	|	abcw		|	abr		|	2				|	8			|
|	0	|	4	|	abcw		|	fntx		|	0				|	16			|
|	0	|	5	|	abcw		|	abcdef	|	3				|	16			|
--- etc etc

"""

def build_letter_sets(words):
	letter_sets = []
	for word in words:
		letter_sets.append(set(word))
	return letter_sets

def calculate_max_product(letter_sets,words):
	max_product = 0
	for i in range(len(words)-1):
		for j in range(i+1, len(words)):
			if len(words[i]) * len(words[j]) > max_product:
				if len(letter_sets[i].intersection(letter_sets[j])) == 0:
					max_product = len(words[i]) * len(words[j])
	return max_product

class Solution(object):
	def maxProduct(self, words):
		if len(words) == 0:
			return 0
		else:
			letter_sets = build_letter_sets(words)
			max_product = calculate_max_product(letter_sets,words)
			return max_product

# # FAST SOLUTION
# class Solution(object):
# 	def maxProduct(self,words):
# 		charsets = reduce(lambda )
