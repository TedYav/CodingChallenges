import timeit
import itertools
import random

# arr = [random.randint(0,1000) for i in range(1000000)]
# print("ARR generated")

# def a():
#   out = arr[1:]
#   # count = 0
#   # for i in out:
#   #   count += 1
#   # print("A %d" % count)

# def b():
#   out = itertools.islice(arr,1,None)
#   # count = 0
#   # for i in out:
#   #   count += 1
#   # print("B %d" % count)

def a():
  arr = [[0] * 1000 for i in range(1000)]

def b():
  arr = [[0 for j in range(1000)] for i in range(1000)]

time1 = timeit.timeit(a,number=10)
time2 = timeit.timeit(b,number=10)

print("TIME1 %f\nTIME2 %f" % (time1,time2))
