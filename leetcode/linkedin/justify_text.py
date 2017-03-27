"""

JUSTIFY:
STRATEGY:
    * Iterate through words
    * Calculate how many words we can fit on one line = sum(len(words)) + # words - 1 <= L
    * Space the words evenly --> build as list then join as string
    * Return last line left justified
    * Lines that contain one word are also left justified

ASSUMING: no words longer than line length --> otherwise we could split and use dash at end (not in corner cases)

"""

class Solution(object):
    def fullJustify(self, words, max_width):
        """
        :type words: List[str]
        :type max_width: int
        :rtype: List[str]
        """
        output = []
        current_line_length = 0
        current_line = []
        for word in words:
            new_length = calculate_line_length(current_line_length,word)
            if new_length <= max_width:
                current_line_length = new_length
                current_line.append(word)
            else:
                if len(current_line) > 0:
                    output.append(build_line(current_line,max_width))
                current_line_length = len(word)
                current_line = [word]
        if len(current_line) > 0:
            output.append(build_line(current_line,max_width,True))
        return output

def calculate_line_length(prefix_length,word):
    line_length = len(word)
    if prefix_length > 0:
        line_length += prefix_length + 1
    return line_length
    
def build_line(line,target_length,last_line = False):
    output = []
    if len(line) == 0:
        output.append(' ' * target_length)
    elif len(line) == 1:
        output.append(line[0])
        output.append(' ' * (target_length - len(output[0])))
    elif not last_line:
        # redoing calculation, but clearer separation :) --> premature optimization root of all evil
        space_points = len(line) - 1
        spaces_needed = target_length - sum(map(len,line))
        spaces_per_word = spaces_needed // space_points
        words_getting_extra = spaces_needed % space_points
        for word,spaces in zip(line,(spaces_per_word * (1 if i < space_points else 0) + (1 if i < words_getting_extra else 0) for i in range(space_points + 1))):
            output.append(word)
            if spaces > 0:
                output.append(' ' * spaces)
    else:
        length = 0
        for word in line:
            output.append(word)
            output.append(' ')
            length += len(word) + 1
        if length > target_length:
            output.pop()
        elif length < target_length:
            output.append(' ' * (target_length - length))
    return ''.join(output)

def test_justify():
    sut = Solution()
    
    def test(words,length,expected):
        result = sut.fullJustify(words,length)
        print(result)
        print(expected)
        assert len(result) == len(expected)
        for line1,line2 in zip(result,expected):
            assert line1 == line2
    
    test(["What","must","be","shall","be."],12,["What must be","shall be.   "])

# test_justify()
