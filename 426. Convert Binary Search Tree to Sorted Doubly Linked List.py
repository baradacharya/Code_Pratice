"""
step1: inorder tranversal by recursion to connect the original BST
step2: connect the head and tail to make it circular
 Using dummy node to handle corner case
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        dummy = Node(0,None,None)
        self.prev = dummy
        self.DFS(root)
        self.prev.right = dummy.right
        dummy.right.left = self.prev
        return dummy.right

    def DFS(self,root):
        if not root:
            return
        self.DFS(root.left)
        self.prev.right =root
        root.left = self.prev
        self.prev = root
        self.DFS(root.right)