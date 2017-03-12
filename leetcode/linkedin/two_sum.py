"""

    This is a straightforward problem.
    Store numbers in hash set.
    
    To look up, iterate through hash set. At each number, look if complement is in set. Return True if one found else False.
    
    SHOULD'VE ASKED MORE QUESTIONS:
        * duplicates allowed (yes)
        * single number ok (no)
    FIX: use HashMap. Store count of each.

"""

class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__nums = {}
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.__nums[number] = self.__nums.get(number,0) + 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.__nums:
            if value - num in self.__nums:
                if value - num != num or self.__nums[value - num] > 1:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
