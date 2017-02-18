"""

    MAZE:
        Given start and end, find minimum length path to end, or -1 if none
        Direction can only change when hitting a wall
        We choose start direction
    
    SOLUTION:
        Dynamic Programming. Initialize NxM matrix with values [-1,-1,-1,-1] (for real code, we'd use direction object)
            ==> correspond to shortest path to this point when ball is moving [up,down,left,right]
        Set value at start to [0,0,0,0]
        Use stack with (direction,coordinate)
        Initialize stack with all directions and start coordinate.
        While stack is non empty:
            Push all possible new coordinates from current coordinate, given that I'm moving in direction.
            If a coordinate has already been visited from this direction, do not push it to the stack. (Cannot be faster)
            If we are on end coordinate, return the min value on end coordinate that is not -1. It will be in current dir.
        When stack is empty, -1. We would have already reached end by now if it were possible.
    
    TIME COMPLEXITY: O(nm)

"""

def test_shortest_distance():
    solution = Solution()
    sd = solution.shortestDistance
    
    # simplest possible example
    maze = [[0,0]]
    start = (0,0)
    end = (0,1)
    expected = 1
    assert sd(maze,start,end) == expected, "TC1"        #FAIL

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        directions = [0,1,2,3] # UP DOWN RIGHT LEFT
        
        width = len(maze[0])
        height = len(maze)
        distances = [[[-1,-1,-1,-1]for col in range(width)] for row in range(height)]
        distances[start[0]][start[1]] = [0,0,0,0]
        
        # refactor this --> get next coords somehow
        stack = [(direction, start) for direction in directions if not self.is_wall(self.get_next_coordinate(start,direction),maze)]
        while stack:
            direction, coordinate = stack.pop()
            curr_distance = distances[coordinate[0]][coordinate[1]][direction]
            if curr_distance == 0:
                prev_distance = -1
            else:
                prev_coordinate = self.get_prev_coordinate(coordinate,direction)
                prev_distance = distances[prev_coordinate[0]][prev_coordinate[1]][direction]
                
            if coordinate == destination:
                return prev_distance + 1
            else:
                distances[coordinate[0]][coordinate[1]][direction] = prev_distance + 1
                
            next_coordinates = self.get_next_coordinates(coordinate,direction,maze,distances)
            stack.extend(next_coordinates)
        return -1

    def get_prev_coordinate(self,coordinate,direction):
        if direction == 0: #UP
            return (coordinate[0]-1,coordinate[1])
        elif direction == 1: #DOWN
            return (coordinate[0]+1,coordinate[1])
        elif direction == 2: #RIGHT
            return (coordinate[0],coordinate[1]-1)
        elif direction == 3: #LEFT
            return (coordinate[0],coordinate[1]+1)
    
    def get_next_coordinate(self,coordinate,direction):
        if direction in [0,1]: next_coord = self.get_prev_coordinate(coordinate,1-direction)
        else: next_coord = self.get_prev_coordinate(coordinate,3-direction + 2)
        return next_coord
    
    def get_next_coordinates(self,coordinate,direction,maze,distances):
        next_coord = self.get_next_coordinate(coordinate,direction)
        if self.is_wall(next_coord,maze): # can go in any direction
            next_coords = [(new_direction, self.get_next_coordinate(coordinate,new_direction)) for new_direction in range(4)]
            next_coords = filter(lambda data: not self.is_wall(data[1],maze) and not self.is_visited(data[1],data[0],distances), next_coords)
            return next_coords
        else:
            return [(direction,next_coord)] if not self.is_visited(next_coord,direction,distances) else []
            
    def is_wall(self,coordinate,maze):
        if self.out_of_bounds(coordinate,maze):
            return True
        else:
            return maze[coordinate[0]][coordinate[1]] == 1
    
    def is_visited(self,coordinate,direction,distances):
        if self.out_of_bounds(coordinate,distances):
            return True
        else:
            return distances[coordinate[0]][coordinate[1]][direction] != -1
            
    def out_of_bounds(self,coordinate,maze):
        return coordinate[0] < 0 or coordinate[1] < 0 or coordinate[0] >= len(maze) or coordinate[1] >= len(maze[0])
        