"""

   n = 10, k=2, move element max of 2 positions
   
   [3, 1, 4, 6, 7, 5] k = 2
   
   [3, 1, 4, 6, 7]
   
   [3, 1, 4] => [1, 3, 4]
   
   [1, 3, 4]
   s
      s
         s
    
    s
   [2, 3, 1, 5]
     
   [1, 2, 3, 5]
     
   [4, 6, 7] => [4, 6, 7]
   
   [1, 3, 4, 5, 6, 7]
   
   General case: unsorted array --> k = n --> nlogn
   
   Look at each block size k:
      Find middle element O(k)
      Partition O(k)
   
"""

import queue

def k_messed_sort(arr, k):
   if not arr or k < 0:
      return None
   elif k == 0:
      return arr
   else:
      window = queue.PriorityQueue()
      for i in range(len(arr) + k - 1):
         if i<len(arr):
            queue.put(arr[i])
         if i>= k:
            arr[i-k] = queue.get()
      return arr
         
def solution(arr, k):
   h = heapq()
   n = len(arr)
   for i in range(0, k+1):
      h.insert(arr[i])
   for i in range(k+1, n):
      arr[i-(k+1)] = h.get()
   for i in range(0, k+1):
      arr[n-k-1 + i] = h.get()
   return arr
         
         
         