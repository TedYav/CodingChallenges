class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__q_stack = []
        self.__s_stack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.__s_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.__check_queue()
        return self.__q_stack.pop()
            

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.__check_queue()
        return self.__q_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.__q_stack) == 0 and len(self.__s_stack) == 0
    
    def __check_queue(self):
        if len(self.__q_stack) == 0:
            self.__reverse_stacks()
    
    def __reverse_stacks(self):
        while len(self.__s_stack) > 0:
            self.__q_stack.append(self.__s_stack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
