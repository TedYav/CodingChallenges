"""

    Word Distance:
        Given a list of words and two words (which are *guaranteed* to be in the list) return shortest distance between them.
        
    Strategies:
        Graph --> make words into a graph, run a BFS. Slow.
        Better -> make list of all occurences of each word, look for closest pair
        Best ---> iterate through list, keeping track of last word seen. Each time other word is seen, update shortest distance.
            O(n)
"""
import sys
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        current_word = None
        current_pos = -1
        min_dist = sys.maxsize
        
        word_set = set([word1,word2]) # O(1) lookup
        
        same_words = len(word_set) == 1
        
        for i in range(len(words)):
            if words[i] in word_set:
                if current_word is not None:
                    if (words[i] != current_word or same_words) and i - current_pos < min_dist:
                        min_dist = i - current_pos
                    current_word = words[i]
                    current_pos = i
                else:
                    current_word = words[i]
                    current_pos = i
        
        return min_dist

def test_shortest_distance():
    solution = Solution()
    swd = solution.shortestWordDistance
    
    word_list = ['a','b','a','b','a']
    word1 = 'a'
    word2 = 'b'
    assert swd(word_list,word1,word2) == 1, swd(word_list,word1,word2)          # PASS
    
    word2 = 'a'
    assert swd(word_list,word1,word2) == 2, swd(word_list,word1,word2)          # PASS

test_shortest_distance()
