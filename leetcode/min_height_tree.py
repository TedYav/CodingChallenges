"""

    MinHeightTree:
        For any tree t, there is some minimum depth d that can be established by rooting the tree at various nodes.
        There can only be one or two nodes where the tree can be rooted. We find the longest distance between two leaves:
            L
        Then the minimum conceivable depth is either L//2 (if L is even) or ceil(L/2) if L is odd.
        If we move one node in either direction, then one of the depths will increase by one, the other will decrease.
        Since there are no cycles, we can only pick between two nodes with this property, otherwise there will be some node
        at depth greater than ceil(L/2).
        
    STRATEGY:
        Find All Leaf Nodes
        Look for Longest Path
        If longest path has even number of nodes, choose two middle nodes
        If longest path has odd number of nodes, choose middle node
        
        O(n) find longest path:
            * Root tree arbitrarily, find node with greatest depth
            * Root tree at this node, find new node with greatest depth
            Return these two nodes and new depth value + 1 (== number of nodes along path)
            
        O(n) find min heights:
            

"""

def list_eq_unordered(list1,list2):
    list1 = sorted(list1)
    list2 = sorted(list2)
    print(list1)
    print(list2)
    if len(list1) != len(list2): return False
    for i in range(len(list1)):
        if list1[i] != list2[i]: return False
    return True

def test_find_min_height_trees():
    solution = Solution()
    mht = solution.findMinHeightTrees
    
    assert list_eq_unordered(mht(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]),[3,4]), "TC1"
    
    assert list_eq_unordered(mht(4, [[1, 0], [1, 2], [1, 3]]),[1]), "TC2"
    
    assert list_eq_unordered(mht(1,[]),[0]), "TC3"
    
    assert list_eq_unordered(mht(0,[]),[-1]), "TC4"

    assert list_eq_unordered(mht(4, [[1, 0], [1, 2], [1, 3]]),[1]), "TC2"

test_find_min_height_trees()

class Node:
    def __init__(self, val):
        self.children = []
        self.val = val
        self.depth = -1
        self.pred = None
    
    def add_child(self, node):
        self.children.append(node)
        node.children.append(self)
    
    def reset(self):
        self.depth = -1
        self.pred = None
        for node in self.children:
            if node.depth >= 0:
                node.reset()
    
    def find_max_depth_node(self):
        stack = [self]
        max_depth = -1
        max_depth_node = None
        while stack:
            node = stack.pop()
            node.depth += 1
            if node.depth > max_depth:
                max_depth = node.depth
                max_depth_node = node
            for child in node.children:
                if child.depth == -1:
                    child.depth = node.depth
                    child.pred = node
                    stack.append(child)
        return max_depth_node

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 0: return [-1]
        elif n == 1: return [0]
        else:
            graph = self.build_graph(n,edges)
            deepest_node = self.find_deepest_node(graph)
            midpoints = self.find_midpoints(deepest_node)
            return [node.val for node in midpoints]
    
    def find_deepest_node(self,graph):
        root = graph[0]
        first_point = root.find_max_depth_node()
        root.reset()
        return first_point.find_max_depth_node()
        
    def find_midpoints(self,deepest_node):
        num_steps_to_mid = deepest_node.depth // 2
        current_steps = 0
        result = []
        node = deepest_node
        while current_steps < num_steps_to_mid:
            node = node.pred
            current_steps += 1
        result.append(node)
        
        if deepest_node.depth % 2 == 1:
            result.append(node.pred)
        
        return result
    
    def build_graph(self,n,edges):
        nodes = [Node(i) for i in range(n)]
        for e in edges:
            if min(e[0],e[1]) < 0 or max(e[0],e[1]) >= len(nodes): raise IndexError()
            nodes[e[0]].add_child(nodes[e[1]])
        return nodes