"""

    Sentences On Screen:
        How many times can given sentence (list of words joined by space or newline) fit on screen of size r x c
    
    Simple Solution:
        O(rc)
        ==> lay out sentence on screen, count number of times it goes on
    
    Better:
        Count how long each subsentence is (from word 0 to last word)
        Go row by row filling in sentence
            * Binary search on subsentence lengths for longest less than remainder on row
            * Keep track of:
                * row offset (if row contains the end of a sentence and start of new one)
                * sentence offset (if sentence has been output partially to above lines)
        if sentence has n words:
        O(n + rlogn)

"""

def test_binary_search():
    sut = Solution()
    assert sut.binary_search([1,2,3,5,6],4) == 2, "BS TC1"
    assert sut.binary_search([1,2,3,4,5],6) == 4, "BS TC2"
    
def test_words_typing():
    sut = Solution()

    sentence = ["f","p","a"]
    rows = 8
    cols = 7
    assert sut.wordsTyping(sentence,rows,cols) == 10, "WT TC0"

    rows = 2
    cols = 8
    sentence = ["hello", "world"]
    assert sut.wordsTyping(sentence,rows,cols) == 1, "WT TC1"

    rows = 3
    cols = 6
    sentence = ["a", "bcd", "e"]
    assert sut.wordsTyping(sentence,rows,cols) == 2, "WT TC2"

    rows = 4
    cols = 5
    sentence = ["I", "had", "apple", "pie"]
    assert sut.wordsTyping(sentence,rows,cols) == 1, "WT TC1"

    sentence = ["try","to","be","better"]
    rows = 10000
    cols = 9001
    import timeit
    def a():sut.wordsTyping(sentence,rows,cols)
    time = timeit.timeit(a,number=1)
    print(time)

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        subsentence_lengths = self.calculate_sub_sentence_lengths(sentence)
        count = 0
        row_offset = 0
        sentence_offset = 0
        for i in range(rows):
            while row_offset < cols:
                words_to_fit = self.binary_search(subsentence_lengths,cols - row_offset + sentence_offset)
                if words_to_fit < len(sentence): # can't fit any more in this row
                    sentence_offset = subsentence_lengths[words_to_fit] + 1
                    break
                else:
                    count += 1
                    row_offset += subsentence_lengths[-1] + 1 - sentence_offset
                    sentence_offset = 0
            row_offset = 0
        return count
    
    def calculate_sub_sentence_lengths(self, sentence):
        lengths = [-1]
        for word in sentence:
            lengths.append(lengths[-1] + 1 + len(word))
        lengths[0] = 0
        return lengths
    
    def binary_search(self,array,target):
        low = 0
        high = len(array)-1
        mid = low + (high-low)//2
        while low<high-1:
            if array[mid] < target:
                low = mid
            elif array[mid] > target:
                high = mid - 1
            else:
                return mid
            mid = low + (high-low)//2
        return low if array[high] > target else high

test_binary_search()
test_words_typing()