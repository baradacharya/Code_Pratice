# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root,None,None)
    def isValid(self,root,minnode,maxnode):
        if not root: return True

        if minnode and root.val <= minnode.val or maxnode and root.val >= maxnode.val: #False conditions
            return False

        return self.isValid(root.left,minnode,root) and self.isValid(root.right,root,maxnode)

