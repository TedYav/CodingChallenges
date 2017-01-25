n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
print(sum([c.count(sock)//2 for sock in set(c)]))
