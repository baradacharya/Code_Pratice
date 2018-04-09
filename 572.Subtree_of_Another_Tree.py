# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #T: O(mn), S:O(n)
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s: return False
        return self.subTree(s,t)
    def isEqual(self,s,t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isEqual(s.left,t.left) and self.isEqual(s.right,t.right)

    def subTree(self,s,t):
        return s != None and self.isEqual(s,t) or self.subTree(s.left,t) or self.subTree(s.right,t)