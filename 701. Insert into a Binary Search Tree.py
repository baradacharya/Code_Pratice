# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        return self.insertIntoBSTUtil(root, val, TreeNode(val))

    def insertIntoBSTUtil(self, root, val, node):
        if not root:
            return node
        if root.val > val:
            root.left = self.insertIntoBSTUtil(root.left, val, node)
        else:
            root.right = self.insertIntoBSTUtil(root.right, val, node)
        return root
