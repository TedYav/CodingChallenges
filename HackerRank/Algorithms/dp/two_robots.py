"""

TWO ROBOTS:
    Given N queries, and two robots, determine minimum total distance that must be traversed.
    
    Robots start at position of first query they take.
    
    let F(i,x,y) = minimum distance necessary to process queries Q_i to Q_n-1, inclusive, with robots starting at postitions x and y respectively.
    if x == -1 or y == -1, then robot can start at arbitrary position (no travel distance to start query i)
    ANSWER TO PROBLEM:
    min(F(0,x,y) for all x,y)
    
    F(i,x,y) = min(
                   F(i+1,q_i.end,y) + |x - q_i.start| + |q_i.end - q_i.start|    # ROBOT 1 EXECUTES QUERY i
                   F(i+1,x,q_i.end) + |y - q_i.start| + |q_i.end - q_i.start|    # ROBOT 2 EXECUTES QUERY i
                  )
                  
               if x == -1, then |x - q_i.start| = 0
               if y == -1, then |y - q_i.start| = 0
               
    F(n,x,y) = 0 for all x, for all y

    NOW, we want to iterate in REVERSE, which complicates this somewhat. Where do the robots end?
    WELL, we know that the two robots can start on any position, therefore: they are interchangable.
        Min distance is same regardless of which robot moves first.
    
    THEREFORE: we can say that robot 1 will be the last one to move. Thus we know:
    F(n,x,y) ==> x == q_n-1.end
    F(n,q_n-1.end,-1) = 0
    F(n-1,q_n-1.begin,-1) = q_n-1.length
    F(n-2,)
    
    LET'S OPTIMIZE FURTHER:
    since robots are interchangeable, we know ONE robot has ALWAYS executed the previous query. Let's always assume this is robot 1.
    Thus we only have to run the possibilities for robot 2 (run all y values for y in [1...M]).
    (Further optimization for special cases: only have to run over set of end points visited till now, and start coordinates in future)
    
    y = coord of robot 2
    q_i-1.end = coord of robot 1, given
    F(i,y) = min(
                   F(i+1,y) + |q_i-1.end - q_i.start| + |q_i.start - q_i.end|
                   F(i+1,q_i-1.end) + |y - q_i.start| + |q_i.start - q_i.end|
                )
    Run for all values of y for each.
    
    Return min(F(0,y))

The first line contains a single integer,  (the number of test cases); each of the  test cases is described over  lines.

The first line of a test case has two space-separated integers,  (the number of containers) and  (the number of queries). 
The  subsequent lines each contain two space-separated integers,  and , respectively; each line describes the  query.

"""

import itertools
import sys

def solve():
    t = int(input().strip())
    for _ in range(t):
        m,q = map(int,input().strip().split())
        start = [0] * q
        end = [0] * q
        positions = set()
        for i in range(q):
            start[i],end[i] = map(int,input().strip().split())
            if start[i] not in positions: positions.add(start[i])
            if end[i] not in positions: positions.add(end[i])
        print(minimum_travel_distance(m,start,end,positions))

# either going to start at start position of later query,
# or end position of earlier query

def minimum_travel_distance(num_containers,start,end,positions):
    next_query = [0] * num_containers
    current_query = [0] * num_containers
    min_query = sys.maxsize
    for query_num in range(len(start)-1,-1,-1):
        for start_pos in positions:
            query_dist = abs(end[query_num] - start[query_num])
            if query_num == 0:
                current_query[start_pos-1] = next_query[start_pos-1] + query_dist
                if current_query[start_pos - 1] < min_query:
                    min_query = current_query[start_pos-1]
            else:       
                robot1_dist = next_query[start_pos-1] + abs(end[query_num-1] - start[query_num])
                robot2_dist = next_query[end[query_num - 1]-1] + abs(start_pos - start[query_num])
                current_query[start_pos-1] = min(robot1_dist,robot2_dist) + query_dist
        current_query,next_query = next_query,current_query
    return min_query

import timeit
def timedsolve():
    time = timeit.timeit(solve,number=1)
    print("EXECUTION TIME %f" % time)

# INITIAL TIME: allocate entire M x N memo: 50 sec
# FIRST OPTIMIZATION: memo is only two cols: 44 sec
# NEXT OPTIMIZATION: do not check all values-check possible values: 27 sec

timedsolve()

"""
def possible_start_positions(query_num,start,end):
    return itertools.chain(itertools.islice(start,query_num,len(end)),itertools.islice(end,query_num))

def minimum_travel_distance(num_containers,start,end):
    next_query = [0] * num_containers
    current_query = [0] * num_containers
    min_query = sys.maxsize
    for query_num in range(len(start)-1,-1,-1):
        for start_pos in possible_start_positions(query_num,start,end):
            query_dist = abs(end[query_num] - start[query_num])
            if query_num == 0:
                current_query[start_pos-1] = next_query[start_pos-1] + query_dist
                if current_query[start_pos - 1] < min_query:
                    min_query = current_query[start_pos-1]
            else:       
                robot1_dist = next_query[start_pos-1] + abs(end[query_num-1] - start[query_num])
                robot2_dist = next_query[end[query_num - 1]-1] + abs(start_pos - start[query_num])
                current_query[start_pos-1] = min(robot1_dist,robot2_dist) + query_dist
        next_query = current_query
        current_query = [0] * num_containers
    return min_query
"""
