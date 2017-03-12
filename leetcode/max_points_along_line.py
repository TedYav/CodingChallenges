"""

    NAIVE:
        O(n^3) -- look at all pairs of points, then examine all other points that lie on that line. n^2 pairs, n points ==> n^3
    
    BETTER:
        Keep points in HashSet. Iterate through it. Find all other points that lie along line. Delete from set.
        ISSUE: will eliminate examinine one line twice, but does not solve the issue of having to examine other lines.
    
    BETTER (space inefficient):
        Allocate n^2 space-> set of sets of points. Start with point 1 in set 1. Examine all other points. Each time we find a point along the line, we delete those points from set 1, and delete them from all other sets in which they are members.
        O(n^2)
        
        STRATEGY:
            * allocate point sets
            * create lines
            * trim sets
            * keep track of max

"""


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

"""

TODO:
    Refactor --> need to keep track of index for O(1) lookups.
    This test case is failing: getting 2 instead of 3.

    Input:
    [[1,1],[1,1],[2,3]]
    Output:
    2
    Expected:
    3

"""

# STRATEGY: store points && number of points at each position
# Add up number of points for each point along line
# Don't use array -- too complicated and can be defeated by including a ton of duplicate points
# Be sure we do not add points twice to a set. Recommend doing set based on unique coordinates.

def make_point_sets(points):
    point_sets = []
    for i in range(len(points)):
        remaining_points = points[i+1:]
        point_sets.append(set([(i+1+j,remaining_points[j]) for j in range(len(remaining_points))]))
    return point_sets

# may need to watch out for floating point errors here and use an epsilon value
def point_is_on_line(point1,point2,slope):
    if slope is not None:
        return point2.y - point1.y == slope * (point2.x - point1.x)
    else:
        return point2.x == point1.x
    
def slope(point1,point2):
    if point1.x != point2.x:
        return (point2.y - point1.y)/(point2.x - point1.x)
    else:
        return None

def max_collinear_points(points,point_sets):
    max_points = 2
    for i in range(len(points)):
        current_start = (i,points[i])
        # can leave one element because I've removed myself from its set already during preparation
        while len(point_sets[i]) > 1:
            points_along_line = []
            current_end = point_sets[i].pop()
            current_slope = slope(current_start[1],current_end[1])
            
            for test_point in point_sets[i]:
                if point_is_on_line(current_start[1],test_point[1],current_slope):
                    points_along_line.append(test_point)
            
            if 2 + len(points_along_line) > max_points:
                max_points = len(points_along_line) + 2
            
            points_along_line.append(current_start)
            points_along_line.append(current_end)
            for point1 in points_along_line:
                for point2 in points_along_line:
                    if point1 in point_sets[point2[0]]:
                        point_sets[point2[0]].remove(point1)
    return max_points

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points: return 0
        elif len(points) <= 2: return len(points)
        else:
            point_sets = make_point_sets(points)
            return max_collinear_points(points,point_sets)
