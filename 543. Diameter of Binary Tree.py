# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root : return 0
        self.maxlen = 0
        def DFS(root):
            if not root : return 0
            l = DFS(root.left)
            r = DFS(root.right)
            self.maxlen = max(self.maxlen,l+r+1) #if the current root is the peak of path
            return max(l,r)+1#if current root is not the peak,root is along the path
        DFS(root)
        return self.maxlen-1