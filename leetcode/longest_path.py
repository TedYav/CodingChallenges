"""

    Nearly identical to Google challenge yesterday.
    
    Strategy: split string by \n
    Count tabs to determine depth.
    Use stack to maintain current prefix size
    If len(current file) + current prefix > max_len, max_len is updated
    return max_len

"""

# def test():
#     test_is_file()
#     test_depth()
#     # test_longest_path()

# def test_is_file():
#     s = Solution()
#     assert s.is_file('abc.def')
#     assert not s.is_file('\t\t\t\tabc')

# def test_depth():
#     s = Solution()
#     assert s.depth('abc.jpeg') == 0
#     assert s.depth('\t\t\t\tabc') == 4

class Solution(object):
    def is_file(self,item): return '.' in item
    
    def depth(self, item):
        curr_depth = 0
        for c in item:
            if c != '\t': return curr_depth
            curr_depth += 1
    
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        prefix_stack = [0]
        current_depth = 0
        max_length = 0
        file_tree = input.split('\n')
        for item in file_tree:
            item_depth = self.depth(item)
            
            while item_depth < current_depth:
                current_depth -= 1
                prefix_stack.pop()
                
            path_length = len(item) - item_depth + prefix_stack[-1]    
            
            if self.is_file(item) and path_length > max_length:
                max_length = path_length
            else:
                prefix_stack.append(path_length + 1)
                current_depth += 1
            
        return max_length

# test()