# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        lheight = 0
        rheight = 0
        l = root
        r = root

        while l:
            lheight += 1
            l = l.left

        while r:
            rheight += 1
            r = r.right

        if lheight==rheight:
            return (1 << lheight) - 1

        return self.countNodes(root.left) + self.countNodes(root.right)+1