"""
   Shifted Array Search
   1. Binary Search --> look in middle, adjust low and high accordingly
   2. Shifted Version:
      Option 1: 
         * Use modified binary search to find shift point.
         * Look at min, max for right side, min, max for left side, search in one or the other

   To find shift point:
      Find index i s.t. arr[i] < arr[i-1]
      
    low = 0
    high = len(arr) - 1
   
    [2, 4, 5, 9, 12, 17] 
    
    low = 0
    high = 5
    
    mid = 2
    arr[mid] = 17, arr[high] = 5, arr[low] = 9 --> shift on right side
   
    low = mid = 2 
    mid = 3
    high = 5
    
    arr[low] = 17
    arr[mid] = 2
    arr[high] = 5
    
    high = mid = 3
    low = 2
    high - low = 1 shift found.
    
    Examine left and right and do standard binary search
    [9, 12, 17, 2, 4, 5]
    
    arr = [2,2,2,2,3,5,2]
    arr = [2,2,2,2,2,2,2]
    arr = [2,3,5,2,2,2,2]
    
    shift_point = i s.t. arr[i] < arr[i-1] or i == 0

"""

def find_shift_point(arr,low,high):
   mid = low + (high-low)//2
   if high - low <= 1:
      return low if (low == 0 or arr[low] < arr[low-1]) else -1
   else:
      if arr[mid] > arr[0]:
         return find_shift_point(arr,mid,high)
      elif arr[mid] < arr[0]:
         return find_shift_point(arr,low,mid)
      else:
         return max(find_shift_point(arr,low,mid),find_shift_point(arr,mid,high))
      
def binary_search(arr,target,low,high):
   mid = low + (high-low)//2
   while low <= high:
      if arr[mid] < target:
         low = mid + 1
      else arr[mid] > target:
         high = mid - 1
      else:
         return mid
   return -1

def search_in_shifted_array(arr,num):
   if not arr or len(arr) == 0: return -1
   else:
      shift_point = find_shift_point(arr,0,len(arr)-1)
      
      if shift_point == -1: # all numbers are the same
         return 0 if arr[0] == num else -1
      elif arr[shift_point] < num and arr[-1] > num:
         return binary_search(arr,num,shift_point,len(arr)-1)
      elif shift_point > 0:
         return binary_search(arr,num,0,shift_point - 1)
      else:
         return -1
         