def test_fraction_to_decimal():
    solution = Solution()
    
    # divide by 0 should return None
    assert solution.fractionToDecimal(10,0) is None, "TC1"          # PASS
    
    # numbers divisible --> return integer division
    assert solution.fractionToDecimal(10,2) == "5", "TC2"           # PASS
    assert solution.fractionToDecimal(100,4) == "25", "TC3"         # PASS
    
    # negative numbers which are divisible --> return integer division
    assert solution.fractionToDecimal(-10,2) == "-5", "TC4"         # PASS
    assert solution.fractionToDecimal(10,-2) == "-5", "TC5"         # PASS
    assert solution.fractionToDecimal(-10,-2) == "5", "TC6"         # PASS
    
    # 0 numerator -- should return 0 if denominator not zero
    assert solution.fractionToDecimal(0,100) == "0", "TC7"          # PASS
    assert solution.fractionToDecimal(0,-50) == "0", "TC8"          # PASS
    
    # non-repeating decimal -- should return complete answer in string format
    assert solution.fractionToDecimal(2,10) == "0.2", "TC9"         # PASS
    assert solution.fractionToDecimal(10,4) == "2.5", "TC10"        # PASS
    assert solution.fractionToDecimal(100,40) == "2.5", "TC11"      # PASS
    
    # repeating decimal -- should parenthesize repeating section
    assert solution.fractionToDecimal(10,3) == "3.(3)", "TC12"      # PASS
    assert solution.fractionToDecimal(100,24) == "4.1(6)", "TC13"   # PASS
    
    # repeating decimal with multiple digits in repeat
    assert solution.fractionToDecimal(100,44) == "2.(27)", "TC14"   # PASS

    # negative numbers should not round wrong
    assert solution.fractionToDecimal(-50,8) == "-6.25", "TC15"

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0: return None
        elif numerator == 0: return "0"
        else:
            result = []
        
            # avoids string concatenation
            if min(numerator,denominator) < 0 and max(numerator,denominator) > 0:
                result.append("-")
                numerator, denominator = abs(numerator), abs(denominator)
            result.append(str(numerator//denominator))
            
            if numerator % denominator != 0:
                curr_remainder = numerator % denominator
                result.append(".")
                
                remainders = []
                remainder_results = []
                remainder_set = set()
                
                while curr_remainder != 0 and curr_remainder not in remainder_set:
                    curr_numerator = 10 * curr_remainder
                    remainder_results.append(curr_numerator // denominator)
                    remainder_set.add(curr_remainder)
                    remainders.append(curr_remainder)
                    curr_remainder = curr_numerator % denominator
                
                if curr_remainder == 0:
                    result.extend([str(r) for r in remainder_results])
                else:
                    repeat_index = remainders.index(curr_remainder)
                    result.append("".join([str(r) for r in remainder_results[:repeat_index]]))
                    result.append("(" + "".join(str(r) for r in remainder_results[repeat_index:]) + ")")
        
            return "".join(result)
        
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        """
        STRATEGY:
            1. Divide Numerator by Denominator. Add result to output
            2. Take remainder, multiply by 10. Divide by denominator. Append to output.
            3. Repeat until remainder is the same or remainder is 0.
                If remainder is the same -- then surround previous result in parentheses -- it will repeat
                If remainder is 0, return
        """
        

test_fraction_to_decimal()