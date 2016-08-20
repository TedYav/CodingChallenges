# another 2 liner--using list comprehensions
# I just check that there's a maximum of 1 character with odd # of occurences
s = list(input().strip())
print("YES" if (len(set([c for c in s if s.count(c) % 2])) < 2 ) else "NO")