# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    """
    will use two pointer
    1. keep track of the left most node
    2. will traverse levelorder for traversing
    """
    def connect(self, root):
        if not root: return None
        leftmost  = root
        while leftmost.left: #will stop before last level as we are connecting childlevels
            cur = leftmost
            while cur:
                cur.left.next = cur.right
                if cur.next != None:
                    cur.right.next = cur.next.left
                cur = cur.next
            leftmost = leftmost.left
