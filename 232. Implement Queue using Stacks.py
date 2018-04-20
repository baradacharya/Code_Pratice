#1 (Two Stacks) Push diff- O(n)per operation, Pop easy - O(1) per operation. S:O(n)
#2 two stack ,push easy O(1), pop diff  amortized: O(1)
class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pushstack = []
        self.popstack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.pushstack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.transfer()
        return self.popstack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.transfer()
        return self.popstack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (not self.popstack) and (not self.pushstack)
    def transfer(self):
        if not self.popstack:
            while self.pushstack:
                self.popstack.append(self.pushstack.pop())



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()