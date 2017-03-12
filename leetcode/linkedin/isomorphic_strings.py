"""

    ISOMORPHIC STRING:
        Strategy:
            * Convert characters to numbers based on occurence order
            * Compare resulting arrays
            * If equal, return True, else False
        Optimizations:
            * Return False immediately if different lengths
            * Compare while running (in case strings are very long)
            
        O(n) upper bound
        Omega(m) lower bound where m == number of characters before mismatch (O(n) if words are isomorphic)

    FURTHER OPTIMIZATION:
        * Could Just Map s to t directly. Don't use intermediate. Faster.

"""
"""
tc_num = 1

def test_isomorphic():
    sut = Solution()
    def test(s,t,expected):
        global tc_num
        assert sut.isIsomorphic(s,t) is expected, "TC%d FAILED" % tc_num
        print("TC%d PASSED" % tc_num)
        tc_num += 1
    
    test("egg","add",True)              # PASS
    test("foo","bar",False)             # PASS
    test("paper","title",True)          # PASS
    test("","test",False)               # PASS
    test("abc"," abc",False)            # PASS
    test("abc", " ab",True)             # PASS
    test("aaab","baaa",False)           # PASS
    test("","",True)                    # PASS

"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None or len(s) != len(t): return False
        else:
            s_chars = {}
            t_chars = {}
            s_index = 1
            t_index = 1
            
            for i in range(len(s)):
                if s[i] not in s_chars:
                    s_chars[s[i]] = s_index
                    s_index += 1
                if t[i] not in t_chars:
                    t_chars[t[i]] = t_index
                    t_index += 1
                if s_chars[s[i]] != t_chars[t[i]]:
                    return False
            return True

# test_isomorphic()
