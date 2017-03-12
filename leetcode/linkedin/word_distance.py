"""

    Shortest Distance
    Since we only have to do it ONCE, just set min_distance = len(words)
    Iterate through list looking for word1 or word2. Keep track of last word (of word1 or word2) seen.
        * If it's different, update min_distance if it's less
        * If it's the same, update the position of the previous word seen
    Return min_distance

"""
"""
tc_num = 0

def test_shortest_distance():
    sut = Solution()
    def test(words,word1,word2,expected):
        global tc_num
        assert sut.shortestDistance(words,word1,word2) == expected, "TC%d FAILED %r %r %r" % (tc_num,words,word1,word2)
        print("TC%d PASSED %r %r %r" % (tc_num,words,word1,word2))
        tc_num += 1
    
    test(['a','b'],'a','b',1)           # PASS
    test(["practice", "makes", "perfect", "coding", "makes"],'coding','practice',3)     # PASS
    test(["practice", "makes", "perfect", "coding", "makes"],'coding','makes',1)        # PASS
"""

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        prev_word_seen = ""
        prev_word_pos = -len(words)
        min_distance = len(words)
        
        target_words = set([word1,word2])
        for i in range(len(words)):
            if words[i] in target_words:
                if prev_word_seen != words[i]:
                    if i - prev_word_pos < min_distance:
                        min_distance = i - prev_word_pos
                    prev_word_seen = words[i]
                prev_word_pos = i
        return min_distance    
        
# test_shortest_distance()
