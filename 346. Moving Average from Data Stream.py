class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        import collections
        self.queue = collections.deque()
        self.sum = 0
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        self.sum += val
        l = len(self.queue)
        if l > self.size:
            self.sum -= self.queue.popleft()
            l -= 1
        return self.sum * 1.0 /l

# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
print obj.next(1)
print obj.next(10)
print obj.next(3)
print obj.next(5)
