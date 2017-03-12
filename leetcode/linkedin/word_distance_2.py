"""

    Word Distance:
        Find shortest distance between ALL PAIRS of words.
        Return as fast as possible.
    
    Since we're calling repeatedly, first instinct is hash table. O(1) lookups.
    BUT—how do we generate the hash table?
    
    NAIVE:
        O(n^2) --> look at each word. Keep track of shortest distance to every other word.
    BETTER:
        Variant of Dijkstra's Algorithm. Actually doesn't apply here, because if this were a graph, it's a line.
        If we combine words into nodes, we'll get meaningless paths. Even if it's directional.
            e.g. practice->makes->coding incorrect distance
        Instead:
            Create two hash tables. One stores positions of elements. Other stores distances.
            For each word:
                Update positional hash table.
                Iterate through positional hash table, updating distances as needed.
            O(n^2) with some optimizations.
            Tighter Bound ==> O(n + m^2) where m == number of unique words.
            OPTIMIZATION:
                Only scan till previous instance of this word. Because those distances already logged.
            Return in O(1) time for any lookup.
        
        BETTER (potentially, if we can sacrifice some lookup time) --> lazily generate the table. Keep track of how much has been generated. Update on the fly. Not going to save a lot of time.

"""

# MEMORY SOLUTION:
# Assign each word ID #. Store those in table--> not word. Also store distance only one way.

"""

    OPTIMIZED SOLUTION:
        Store Positions of Each Word (O(n))
        Memoize Searches for Each Pair --> each search is O(count(word1)*count(word2))
 the first time it is called, and O(1) after

"""

class WordDistance(object):
    def __init__(self,words):
        """
        :type words: List[str]
        """
        self.__distance_table = {}
        self.__position_table = {}
        self.__max_length = len(words)
        self.__calculate_positions(words)

    def __calculate_positions(self,words):
        """
        :type words: List[str]
        """
        for i in range(len(words)):
            if words[i] in self.__position_table:
                self.__position_table[words[i]].append(i)
            else:
                self.__position_table[words[i]] = [i]

    def __compute_distance(self,word1,word2):
        """
        :type word1: str
        :type word2: str
        """
        min_distance = self.__max_length
        positions1 = self.__position_table[word1]
        positions2 = self.__position_table[word2]
        i = j = 0
        while i < len(positions1) and j < len(positions2):
            current_distance = abs(positions1[i] - positions2[j])
            if current_distance < min_distance:
                min_distance = current_distance
            if positions1[i] < positions2[j]:
                i += 1
            else:
                j += 1
        
        return min_distance

    def __set_distance(self,word1,word2,distance):
        if word1 not in self.__distance_table:
            self.__distance_table[word1] = {}
        if word2 not in self.__distance_table:
            self.__distance_table[word2] = {}

        self.__distance_table[word1][word2] = distance
        self.__distance_table[word2][word1] = distance

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 not in self.__distance_table or word2 not in self.__distance_table[word1]:
            self.__set_distance(word1,word2,self.__compute_distance(word1,word2))
        return self.__distance_table[word1][word2]

class WordDistancePrecomputed(object):
    
    def __update_position_table(self,word,position):
        self.__position_table[word] = position
    
    def __update_distance_table(self,word):
        position = self.__position_table[word]
        
        if word not in self.__distance_table:
            self.__distance_table[word] = {}
        
        for target_word in self.__position_table:
            if target_word == word: continue
            else:
                current_distance = position - self.__position_table[target_word]
                
                if target_word in self.__distance_table[word]:
                    prev_distance = self.__distance_table[word][target_word]
                else:
                    prev_distance = current_distance + 1
                
                if current_distance < prev_distance:
                    self.__distance_table[word][target_word] = current_distance
                    self.__distance_table[target_word][word] = current_distance
    
    def __build_tables(self,words):
        for i in range(len(words)):
            self.__update_position_table(words[i],i)
            self.__update_distance_table(words[i])
    
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.__distance_table = {}
        self.__position_table = {}
        self.__build_tables(words)
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return self.__distance_table[word1][word2]


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
