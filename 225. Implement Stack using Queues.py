#1.Two Queues,push : O(1), pop:O(n)
#2.Two Queues,push : O(n), pop:O(1)
#3.One Queues,push : O(n), pop:O(1)
class MyStack(object): #one queue
    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self._queue = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self._queue.append(x)
        #pop data from front of queue and push back at end
        for _ in range(len(self._queue)-1):
            self._queue.append(self._queue.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self._queue.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self._queue

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(10)
obj.push(20)
obj.push(30)
print obj.pop()
print obj.top()
print obj.empty()