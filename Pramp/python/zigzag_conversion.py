"""

    ZigZag Conversion:
    Strategy:
        *Allocate lists for each row
        *Add one char of string to row 1, row 2, row 3...row m
        *Reverse once we reach row m --> m-1, m-2,....1
        *Repeat until we're out of chars
        *Return rows concatenated sequentially

"""

def test_convert():
    sut = Solution()
    c = sut.convert
    
    s = "ABC"
    n = 3
    expected = "ABC"
    assert c(s,n) == expected, "TC1"        # PASS
    
    s = "ABC"
    n = 2
    expected = "ACB"
    assert c(s,n) == expected, "TC2"        # PASS
    
    s = "PAYPALISHIRING"
    n = 3
    expected = "PAHNAPLSIIGYIR"
    assert c(c,n) == expected, "TC3"        # PASS
    
    s = "AB"
    n = 1
    expected = "AB"
    

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0 or len(s) < numRows or numRows == 1: return s
        rows = [[]for i in range(numRows)]
        direction = 1
        current_row = 0
        for c in s:
            rows[current_row].append(c)
            current_row += direction
            if current_row == numRows - 1 or current_row == 0:
                direction *= -1
        return "".join(["".join(row) for row in rows])
