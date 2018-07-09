# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
For given node we check whether its left child is a leaf.
If it is the case, we add its value to answer, otherwise recursively call method on left child.
For right child we call method only if it has at least one nonnull child.
"""
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        ans = 0
        if root.left:
            if not root.left.left and not root.left.right:  # leave
                ans += root.left.val
            else:
                ans += self.sumOfLeftLeaves(root.left)
        if root.right:
            ans += self.sumOfLeftLeaves(root.right)
        return ans