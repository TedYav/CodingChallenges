h = [int(h_temp) for h_temp in input().strip().split()]
word = input().strip()

print(max([h[ord(c) - ord('a')] for c in word]) * len(word))