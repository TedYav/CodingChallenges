i,j,k = map(int,input().strip().split())
def reversed(n): return int(str(n)[::-1])
def is_beautiful(n): return abs(n - reversed(n)) % k == 0
print(len(list(filter(is_beautiful, range(i,j+1)))))

# unreadable two line version
# i,j,k = map(int,input().strip().split())
# print(len(list(filter(lambda n: abs(n - int(str(n)[::-1])) % k==0, range(i,j+1)))))