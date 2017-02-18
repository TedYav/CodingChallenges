"""

    Hit Counter
    Must count hits from last 300 seconds
    Hits are monotonically increasing
    
    We can drop a hit at any point, so cannot combine hits from different times
    
    Strategy:
        Use LLQueue (O(1)) insertion, O(1) get_head, get_tail, peek, etc
        Append Hit objects, time_stamp, hit_count
        Since timestamp is monotonically increasing, if new hit time_stamp is same as time_stamp at head of queue
            Just increase count
            Otherwise: append to queue, drop previous
    

"""

def test_hit_counter():
    HC = HitCounter()
    HC.hit(1)
    assert HC.getHits(1) == 1, "TC1"        # PASS
    
    HC = HitCounter()
    HC.hit(1)
    HC.hit(1)
    HC.hit(1)
    assert HC.getHits(3) == 3, "TC2"        # PASS
    
    HC = HitCounter()
    HC.hit(1)
    HC.hit(1)
    HC.hit(1)
    assert HC.getHits(301) == 0, "TC3"      # PASS

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class LLQueue(object):
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
    
    def push(self, value):
        if self.__head is None:
            self.__head = Node(value)
            self.__tail = self.__head
        else:
            self.__tail.next = Node(value)
            self.__tail.next.prev = self.__tail
            self.__tail = self.__tail.next
        self.__size += 1
    
    def pop(self):
        if self.__head is not None:
            value = self.__head.value
            if self.__head != self.__tail:
                self.__head = self.__head.next
                self.__head.prev = None
            else:
                self.__head = None
                self.__tail = None
            self.__size -= 1
            return value
    
    def peek_back(self):
        if self.__tail is not None:
            return self.__tail.value
    
    def peek_front(self):
        if self.__head is not None:
            return self.__head.value
    
    def size(self):
        return self.__size

class Hit(object):
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.count = 1

class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__total_hits = 0
        self.__hits = LLQueue()
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.__total_hits += 1
        if self.__hits.size() > 0 and self.__hits.peek_back().timestamp == timestamp:
            self.__hits.peek_back().count += 1
        else:
            self.__hits.push(Hit(timestamp))
            
        if timestamp > 300: self.__purge_old_hits()

    def __purge_old_hits(self,timestamp=None):
        if self.__hits.size() > 0:
            if timestamp is None:
                timestamp = self.__hits.peek_back().timestamp
            while self.__hits.size() > 0 and self.__hits.peek_front().timestamp <= timestamp - 300:
                hit = self.__hits.pop()
                self.__total_hits -= hit.count

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        self.__purge_old_hits(timestamp)
        return self.__total_hits
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)