import timeit
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        current_length = 0
        char_set = set()
        start_index = 0
        for i in range(len(s)):
            if s[i] not in char_set:
                char_set.add(s[i])
                current_length += 1
                if current_length > longest:
                    longest = current_length
            else:
                while s[start_index] != s[i]:
                    char_set.remove(s[start_index])
                    start_index += 1
                    current_length -= 1
                start_index += 1 # skip duplicate char
        return longest

# LOL SOLUTION WAS OKAY
# timed out for no reason :(

test = "jvcxnpglnbnfxjkxspbuoiphimjhvgteewbrnhcajqhibugtjjqzrfgctploygteewvrgaupsbztxhohqegkm"
solution = Solution()
def a(): return solution.lengthOfLongestSubstring(test)
time = timeit.timeit(a,number=15)
print("TIME ELAPSED: %s" % time)