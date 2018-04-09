# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = [] #list is a mutable object
        self.inorder(root, res)
        return res

    def inorder(self, root, res):
        if not root: return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)
        return