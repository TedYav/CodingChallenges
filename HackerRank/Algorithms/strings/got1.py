# list comprehension technique too slow, using dict
import collections
count = collections.Counter(input().strip())
print("YES" if (len([k for k in count if count[k]%2]) < 2) else "NO")