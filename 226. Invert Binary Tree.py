#Definition for a binary tree node.
# Trick use an extra variable to keep track of left and right side
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        temp_right = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = temp_right
        return root