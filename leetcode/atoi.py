"""

    BASES: 
        * which: decimal? binary? hex?
        * how is base indicated?
        * what are allowed positioninings of base indicator if it exists?
        
    NEGATIVE NUMBERS: 
        * should we handle them?
        * how are they indicated?
        * what are acceptable positionings of negative indicator? Can there be a space in between?
        
    WHITESPACE:
        * how does whitespace affect the various components of the number string?
        * is trailing / leading whitespace ignored?
        
    DECIMAL POINT:
        * how do we respond to a decimal point? Do we truncate? Do we raise ValueError?
        
    OTHER CHARACTERS:
        * what if string is arbitrary non-numeric characters? Do I raise value error?
        * what if I get valid numeric characters without valid base identifier? Raise error?
        * what if there is a complete number in the string that is parseable, but then there are other characters?
        
    LEADING ZEROES:
        * are leading zeroes acceptable?
        
    OVERFLOW:
        * what if number is too large for 32 bit int? Should I raise ValueError or switch automatically to long?
        
    MORE THAN ONE NUMBER IN STRING:
        * do I convert all numbers separately and return an array? Do I ignore? Do I convert first number?
        
    EMPTY / BAD INPUT:
        * does empty string have numberic value?
        * what about None?
    

FORMAL DEFININITION:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

"""

def test_atoi():
    sut = Solution()
    atoi = sut.myAtoi
    def test(s,expected,tc_num):
        assert atoi(s) == expected, "TC%d" % tc_num
        print("TC%d PASSED ('%s', %d)" % (tc_num,s,expected))
    
    s = ''
    expected = 0
    test(s,expected,1)      # PASS
    
    s = '0'
    expected = 0
    test(s,expected,2)      # PASS
    
    s = '     0'
    expected = 0
    test(s,expected,3)      # PASS
    
    s = '    123'
    expected = 123
    test(s,expected,4)      # PASS
    
    s = '    -0000123'
    expected = -123
    test(s,expected,5)      # PASS
    
    s = '000001235.123'
    expected = 1235
    test(s,expected,6)      # PASS
    
    s = '2147483647'
    expected = 2147483647
    test(s,expected,7)      # PASS
    
    s = '-2147483648'
    expected = -2147483648
    test(s,expected,8)      # PASS
    

DIGIT_TABLE = {str(n):n for n in range(10)}
INT_MAX_DIGITS = [2,1,4,7,4,8,3,6,4,7]
INT_MAX =  2147483647
INT_MIN = -2147483648

def strip_whitespace(s):
    for i in range(len(s)):
        if s[i] != ' ': return s[i:]
    return ""

def read_sign(s):
    if s[0] == '-': return -1
    else: return 1

def strip_sign(s):
    return s[1:] if s[0] in ['-','+'] else s

def remove_leading_zeroes(result):
    i = 0
    while i < len(result) and result[i] == '0':
        i += 1
    return result[i:]

def read_number(s):
    result = []
    found_nonzero = False
    for c in s:
        if c in DIGIT_TABLE:
            result.append(c)
        else:
            break
    return remove_leading_zeroes(result)

def out_of_range(s):
    if len(s) > 10:
        return True
    elif len(s) == 10:
        for i in range(10):
            if DIGIT_TABLE[s[i]] < INT_MAX_DIGITS[i]: return False
            elif DIGIT_TABLE[s[i]] > INT_MAX_DIGITS[i]: return True
            else: continue
    return False

def str_to_number(s):
    pow = 10**(len(s)-1)
    result = 0
    for c in s:
        result += pow * DIGIT_TABLE[c]
        pow = pow // 10
    return result

class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        if s is None or len(s) == 0: return 0
        
        s = strip_whitespace(s)
        if len(s) == 0: return 0
        
        sign = read_sign(s)
        s = strip_sign(s)
        s = read_number(s)
        if len(s) == 0: return 0
        
        if out_of_range(s):
            return INT_MAX if sign == 1 else INT_MIN
        else:
            return sign * str_to_number(s)
            
# test_atoi()
