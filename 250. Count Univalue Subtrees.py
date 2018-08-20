# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        count = [0]
        self.DFS(root, count)
        return count[0]

    def DFS(self, root, count):
        if not root:
            return True
        left = self.DFS(root.left, count)
        right = self.DFS(root.right, count)

        if left and right:
            if root.left and root.val != root.left.val:
                return False
            if root.right and root.val != root.right.val:
                return False
            count[0] += 1
            return True
        else:
            return False