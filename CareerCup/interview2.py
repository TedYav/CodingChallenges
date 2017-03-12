"""
n == 7
.......

circular -> spot n-1 is near spot 0

Q events.
1) car arrives at the spot number i -> if the spot is free car parks, otherwise car goes to i + 1 and so on. if no spot return -1
2) car leaves spot # i.

arrive 2, arrive 2, arrive 2, leave 2, arrive 2

..XXX..
0123456

2, 3, 4, 2

BRUTE FORCE WAY:
    return a list [0 for i in range(n)]
    arrive -> start at idx, iterate until I find an empty space.
    
BETTER WAY:
    - initally: store 0 to n-1 in binary search tree type data structure 
    - arrive: 
        - search for idx in (array? data structure) of available spaces, return first entry which is >= idx
        - if none found, repeat process except searching for 0
        - if none found still -> return -1
        - time complexity here is O(m) where m == number of available spaces at any point in time
    - leave:
        - add entry idx to data struct of available spaces
        - O(logm) --> m is number of available spaces        
        
    0 -> 1 -> 2 --- ignore edge case

"""

"""
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinTree:
    def __init__(self,num_nodes):
        root_value = num_nodes // 2
        self.__root = 

----------------------

directed graph n
that between v, u there is an edge and always 1
v -> u or v <- u

def hasEdge(v, u):
    return bool
    
v -> u ==> hasEdge(v,u) == true
u -> v ==> hasEdge(v,u) == false
    
    
find all vertexes that all other vertices have ingoung edge from
5 0->5, 1->5, etc (n-1 ingoing edges)

BRUTE FORCE:
    Examine every vertex pair, keep track.
    
BETTER STRATEGY:
    - Pick arbitrary vertex
    - Check all edges that could come from this vertex O(n), add all outgoing edges to HashSet

a -> b -> c -> a

BEST STRATEGY:


"""

def giveAllVertices(n):
    


import OrderedSet
# assume insert(i) --> add entry at index i in log(n)

spaces = OrderedSet()

# n == 7
# {0,1,2,3,4,5,6}
def prep(n):
    global spaces
    for i in range(n):
        spaces.insert(i)
    return spaces
    # TODO

# [0,1,2,3] target = 3     # PASS
# [0,1,2,3] target = -1    # PASS
# [0,1,2,3] target = 4     # PASS
def binary_search_gte(arr,target):
    if len(arr) == 0: return -1
    low = 0
    high = len(arr) - 1
    guess = low + (high - low)//2
    while high > low:
        if arr[guess] >= target and (guess == 0 or arr[guess - 1] < target):
            return guess
        elif arr[guess] >= target:
            high = guess - 1
        else:
            low = guess + 1
    return low if arr[low] >= target else -1

def arrive(idx):
"""
    int idx ->
    :rtype int: index of parking spot or -1
"""
    global spaces
    if len(spaces.keys()) == 0: return -1
    else:
        parking_index = binary_search_gte(spaces.keys(),idx)
        if parking_index == -1:
            parking_index = binary_search_gte(spaces.keys(),0)
        return parking_index


def leave(idx):
    global spaces
    
    spaces.insert(idx)


# overall comlexity
# q == # of events
def main():
    q, n
    prep(n)
    for i in range(q):
        # call either arrive or leave
    
