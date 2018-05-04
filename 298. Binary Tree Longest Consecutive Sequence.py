# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node,parent,length):
            if not node:return length
            if parent and node.val == parent.val + 1: length += 1
            else:length = 1
            return max(length,dfs(node.left,node,length),dfs(node.right,node,length))
        return dfs(root,None,0)