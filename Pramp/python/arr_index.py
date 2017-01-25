def array_index(arr, i):
   if not arr:
      return -1
   else:
      low = 0
      high = len(arr)
      while high-low > 0: #high-low >= 0 
         mid = (high + low)//2
         if arr[mid] > mid:
            high = mid - 1
         elif arr[mid] < mid:
            low = mid + 1
         else:
            return mid
      return low if arr[low] == low else -1
# return index i s.t. arr[i] == i, else -1