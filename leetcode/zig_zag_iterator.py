"""

    ZigZag iterator.
    Works for any number of input lists, though this implementation is for 2 to solve hacker rank problem.

    Uses circular linked list to keep track of position in each list. When a list is completely examined,
    we delete node from linked list. 

"""

class KVNode(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.__lists = filter(lambda l: len(l) > 0, [v1,v2])
        self.__current_index_node = self.__build_indices()
    
    def __build_indices(self):
        nodes = []
        for i in range(len(self.__lists)):
            node = KVNode(i,0)
            if i > 0:
                node.prev = nodes[-1]
                node.prev.next = node
            nodes.append(node)
        if len(nodes) > 0:
            nodes[0].prev = nodes[-1]
            nodes[-1].next = nodes[0]
            return nodes[0]
        else:
            return None
    
    def __delete_current_index(self):
        node = self.__current_index_node
        if node == node.prev and node == node.next:
            self.__current_index_node = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
    
    def __advance_current_index(self):
        if self.__current_index_node is not None:
            self.__current_index_node = self.__current_index_node.next
    
    def next(self):
        """
        :rtype: int
        """
        if self.__current_index_node is None: return None
        else:
            current_list = self.__current_index_node.key
            current_index = self.__current_index_node.value
            result = self.__lists[current_list][current_index]
            self.__current_index_node.value += 1
            if self.__current_index_node.value >= len(self.__lists[current_list]):
                self.__delete_current_index()
            self.__advance_current_index()
            return result

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.__current_index_node is not None

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())