"""

    Word Break II:
        Given non-empty string s and non-empty non-empty word containing dictionary d, return all possible sentences formable from s.
    
    Solutions:
        Brute Force: try all possible combinations of spaces. O(2^n) to try all possible combinations. Could take O(n) to verify each, so this is O(n2^n) SLOW.
        Better: use dynamic programming and prefix tries. 
        
        Let f(i) be all possible sentences I can from from s starting at letter i.
        Answer to the problem is f(0)
        
        let w(i) be all words I can form starting at letter i in s.
        f(i) =  []      if w(i) == []
                [""]    if i == len(s)
                [w_i + all sentences in f(i+len(w_i)) for all w_i in w(i)] otherwise
                
        can solve forwards or backwards.
        forwards will be recursive and may result in lots of extra work.
        backwards is our better bet. We will store all possibilities at each step.
        
        STRATEGY:
            * Convert wordDict into prefix trie
            * Create list of possible sentences for i = 0 to len(s) - 1 containing empty list at each index
            * Iterate backwards from n-1 to 0
                * Check how many words we can form at letter i using prefix trie, for each of them, compound with other sentences in table
            * Return list_of_sentences[0]
"""

class TrieNode(object):
    def __init__(self,letter="",prefix=""):
        self.children = {}
        self.letter = letter
        self.prefix = prefix + self.letter
        self.complete_word = False
    
    def add_child(self,letter):
        if letter not in self.children:
            self.children[letter] = TrieNode(letter,self.prefix)

"""

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

"""

class PrefixTrie(object):
    def __init__(self,word_list):
        """
        :type word_list: List[str]
        :rtype: PrefixTrie
        """
        self.word_list = word_list
        self._root = TrieNode()
        self.__build_trie()
    
    def __build_trie(self):
        for word in self.word_list:
            self.add_word(word)
    
    def add_word(self,word):
        node = self._root
        for c in word:
            node.add_child(c)
            node = node.children[c]
        node.complete_word = True
    
    def possible_words_at_index(self,s,i):
        """
        :type s: str
        :type i: int
        :type word_trie: PrefixTrie
        :rtype: List[str]
        """
        words = []
        node = self._root
        while i < len(s) and s[i] in node.children:
            node = node.children[s[i]]
            if node.complete_word:
                words.append(node.prefix)
            i += 1
        return words

def make_sentences(start_index,word,possible_sentences):
    if start_index + len(word) == len(possible_sentences):
        return [[word]]
    else:
        return [[word] + sentence for sentence in possible_sentences[start_index + len(word)]]

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_trie = PrefixTrie(wordDict)
        possible_sentences = [[] for i in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            possible_words = word_trie.possible_words_at_index(s,i)
            for word in possible_words:
                possible_sentences[i].extend(make_sentences(i,word,possible_sentences))
        return [" ".join(sentence) for sentence in possible_sentences[0]]
        
"""

    Word Break II:
        Given non-empty string s and non-empty non-empty word containing dictionary d, return all possible sentences formable from s.
    
    Solutions:
        Brute Force: try all possible combinations of spaces. O(2^n) to try all possible combinations. Could take O(n) to verify each, so this is O(n2^n) SLOW.
        Better: use dynamic programming and prefix tries. 
        
        Let f(i) be all possible sentences I can from from s starting at letter i.
        Answer to the problem is f(0)
        
        let w(i) be all words I can form starting at letter i in s.
        f(i) =  []      if w(i) == []
                [""]    if i == len(s)
                [w_i + all sentences in f(i+len(w_i)) for all w_i in w(i)] otherwise
                
        can solve forwards or backwards.
        forwards will be recursive and may result in lots of extra work.
        backwards is our better bet. We will store all possibilities at each step.
        
        STRATEGY:
            * Convert wordDict into prefix trie
            * Create list of possible sentences for i = 0 to len(s) - 1 containing empty list at each index
            * Iterate backwards from n-1 to 0
                * Check how many words we can form at letter i using prefix trie, for each of them, compound with other sentences in table
            * Return list_of_sentences[0]
"""

class TrieNode(object):
    def __init__(self,letter="",prefix=""):
        self.children = {}
        self.letter = letter
        self.prefix = prefix + self.letter
        self.complete_word = False
    
    def add_child(self,letter):
        if letter not in self.children:
            self.children[letter] = TrieNode(letter,self.prefix)

"""

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

"""

class PrefixTrie(object):
    def __init__(self,word_list):
        """
        :type word_list: List[str]
        :rtype: PrefixTrie
        """
        self.word_list = word_list
        self._root = TrieNode()
        self.__build_trie()
    
    def __build_trie(self):
        for word in self.word_list:
            self.add_word(word)
    
    def add_word(self,word):
        node = self._root
        for c in word:
            node.add_child(c)
            node = node.children[c]
        node.complete_word = True
    
    def possible_words_at_index(self,s,i):
        """
        :type s: str
        :type i: int
        :type word_trie: PrefixTrie
        :rtype: List[str]
        """
        words = []
        node = self._root
        while i < len(s) and s[i] in node.children:
            node = node.children[s[i]]
            if node.complete_word:
                words.append(node.prefix)
            i += 1
        return words

def make_sentences(start_index,word,possible_sentences):
    if start_index + len(word) == len(possible_sentences):
        return [[word]]
    else:
        return [[word] + sentence for sentence in possible_sentences[start_index + len(word)]]

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_trie = PrefixTrie(wordDict)
        possible_sentences = [[] for i in range(len(s))]
        for i in range(len(s)-1,-1,-1):
            print(i)
            possible_words = word_trie.possible_words_at_index(s,i)
            for word in possible_words:
                possible_sentences[i].extend(make_sentences(i,word,possible_sentences))
        return [" ".join(sentence) for sentence in possible_sentences[0]]
        

# import timeit.timeit
def test_word_break():
    sut = Solution()
    # solution breaks because we're assembling sentences too early
    # first we need to check IF we can MAKE any sentences :)
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    result = sut.wordBreak(s,words)
    print(result)

test_word_break()
