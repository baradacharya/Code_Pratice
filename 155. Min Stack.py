class MinStack(object):
    """
    idea is to store (value,minvalue) in the stack.
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        min_value = self.getMin()
        if min_value != None:
            min_value = min(min_value,x)
        else:#first entry
            min_value = x
        self.stack.append((x, min_value))
    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            return self.stack.pop()
        else:
            return None
    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[len(self.stack)-1][0]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[len(self.stack)-1][1] #return top minvalue
        else:
            return None

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
# obj.pop()
# param_3 = obj.top()
print obj.getMin()
obj.pop()
print obj.getMin()