#Definition for a binary tree node.
##T: O(m*n), S:O(n)
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.DFS(s, t)

    def DFS(self, s, t):
        return s!= None and (self.equal(s, t) or self.DFS(s.left, t) or self.DFS(s.right, t))

    def equal(self,s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.equal(s.left, t.left) and self.equal(s.right, t.right)
