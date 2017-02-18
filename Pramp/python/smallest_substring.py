"""

   Smallest Substring of All Characters
   
   Brute Force --> look at all substrings O(n^2) and count them O(n) --> total O(n^3)
   arr: [x,y,z], str: xyyzyzyx
                           ^^^
                      {
                         x: 1
                         y: 1
                         z: 1
                      }
                      min_length = 3
                      start_index = 5
   
   Strategy:
      Set start index = 0
      Create dictionary {} to hold characters in arr with counts
         Initialize to 0's
      Iterate through s:
         Add each character in s to dictionary (increment count)
         Check s[start_index]
            if count[s[start_index]] > 1:
               increment start_index and decrement count[s[start_index]] until count[s[start_index]] == 1

   len(arr) == m
   O(nm)
      ==> O(n + m) ## 
            1. chars dict 
            2. Loop through str => check missing chars? => substring?

   O(m + c) space complexity

   arr = [a,b,c] str = "abababa"

"""

def smallest_substring_with_chars(arr,s):
   counts = {c:0 for c in arr}
   missing_letters = set(arr)
   start_index = 0
   stop_index = len(s) - 1
   for i in range(len(s)):
      counts[s[i]] += 1
      if s[i] in missing_letters:
         missing_letters.remove(s[i])
      if len(missing_letters) == 0:
         while counts[s[start_index]] > 1:
            counts[s[start_index]] -= 1
            start_index += 1
        if i - start_index < stop_index - start_index:
            stop_index = i
   return s[start_index:stop_index + 1]