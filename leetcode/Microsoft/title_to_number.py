"""

    EXCEL COLUMN NUMBER:
    TREAT S AS BASE 26 NUMBER.
    Convert to int.

"""

charmap = {chr(c):c - ord('A') + 1 for c in range(ord('A'),ord('Z') + 1)}

tc_num = 0
def test_titleToNumber():
    sut = Solution()
    def test(s,expected):
        global tc_num
        assert sut.titleToNumber(s) == expected, "TC%d FAILED" % tc_num
        print("TC%d PASS" % tc_num)
        tc_num += 1
    
    test("A",1)
    test("Z",26)
    test("AZ",52)

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        pow = 0
        for i in range(len(s)-1,-1,-1):
            result += 26**pow * charmap[s[i]]
            pow += 1
        return result

# test_titleToNumber()
