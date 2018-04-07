# Definition for a  binary tree node

#stack solution
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        x = node.right
        while x:
            self.stack.append(x)
            x = x.left
        return node.val

#iterator solution
def __init__(self, root):
    self.last = root
    while self.last and self.last.right:
        self.last = self.last.right
    self.current = None
    self.g = self.iterate(root)

# @return a boolean, whether we have a next smallest number
def hasNext(self):
    return self.current is not self.last

# @return an integer, the next smallest number
def next(self):
    return next(self.g)

def iterate(self, node):
    if node is None:
        return
    for x in self.iterate(node.left):
        yield x
    self.current = node
    yield node.val
    for x in self.iterate(node.right):
        yield x



# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())