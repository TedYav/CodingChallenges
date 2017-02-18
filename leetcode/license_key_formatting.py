"""

    License Key Formatting:
        Given string S and number K
        Break S into groups of K characters (excluding all dashes)
        First group may be <= K characters
        Make all letters uppercase
        Return formatted String
    
    S is non-empty and contains ONLY alpha chars and dashes.
    K is positive.
        *Do not need to worry about these edge cases.
    
    Strategy (O(n)):
        *Start at end of string.
        *Append character by character to new list
            *Skip hyphens
            *Using list instead of string to avoid concatenation penalty
            *Make all letters uppercase at same time
        *Every time we append K characters, append a '-'
        *Return list as string in reverse order
        
        Time Complexity ==> 2*O(n) == O(n)
    
    (Note: since len(s) <= 12000, we *could* do an O(N^2) solution, but no reason to do so)

"""

def test_license_key_formatting():
    solution = Solution()
    lkf = solution.licenseKeyFormatting
    
    s = 'A'
    k = 5
    o = 'A'
    assert lkf(s,k) == o, "TC1"         # PASS
    
    s = 'a'
    k = 5
    o = 'A'
    assert lkf(s,k) == o, "TC2"         # PASS
    
    s = 'a5-'
    k = 1
    o = 'A-5'
    assert lkf(s,k) == o, "TC3"         # PASS
    
    s = '2-4A0r7-4k'
    k = 4
    o = '24A0-R74K'
    assert lkf(s,k) == o, "TC4"         # PASS

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        output = []
        current_block_length = 0
        for i in range(len(S)-1,-1,-1):
            if S[i] != '-':
                if current_block_length == K:
                    output.append('-')
                    current_block_length = 0
                output.append(S[i].upper())
                current_block_length += 1
        
        return "".join(output[::-1])

    def licenseKeyFormattingInsertion(self,S,K):
        output = []
        current_block_length = 0
        for i in range(len(S)-1,-1,-1):
            if S[i] != '-':
                if current_block_length == K:
                    output.insert(0,'-')
                    current_block_length = 0
                output.insert(0,S[i].upper())
                current_block_length += 1
        
        return "".join(output)


test_license_key_formatting()
import timeit
import random

def time_lkf(size=12000,k=5,iterations=10):
    charset = [chr(c) for c in range(ord('a'),ord('z'))]
    charset += [chr(c) for c in range(ord('A'),ord('Z'))]
    charset += [chr(c) for c in range(ord('0'),ord('9'))]
    charset += ['-']
    s = "".join([charset[random.randint(0,len(charset)-1)] for i in range(size)])
    print(s)
    print(k)

    solution = Solution()
    print(solution.licenseKeyFormatting(s,k))

    print("TIMING:")
    def a(): solution.licenseKeyFormatting(s,k)
    def b(): solution.licenseKeyFormattingInsertion(s,k)
    time1 = timeit.timeit(a,number=iterations)
    time2 = timeit.timeit(b,number=iterations)
    print("APPEND AND REVERSE METHOD: " + str(time1))
    print("INSERT AND COMBINE METHOD: " + str(time2))