# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res  = []
        if not root: return []
        self.preorder(root,res)
        return res

    def preorder(self, root, res):
        if not root: return
        res.append(root.val)
        self.preorder(root.left,res)
        self.preorder(root.right,res)
#without using recusion
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        rights = []
        while root:
            res.append(root.val)
            if root.right:
                rights.append(root.right)
            root = root.left
            if not root and  len(rights) != 0:
                root = rights.pop()
        return res
