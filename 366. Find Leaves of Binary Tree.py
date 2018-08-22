"""
For this question we need to take bottom-up approach. The key is to find the height of each node. Here the definition of height is:
The height of a node is the number of edges from the node to the deepest leaf.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        import collections
        res = collections.defaultdict(list)
        self.heightfromBottom(root,res)
        return res

    def heightfromBottom(self,root,res):
        if not root:
            return -1
        height = 1 + max(self.heightfromBottom(root.left,res),self.heightfromBottom(root.right,res))
        res[height].append(root.val)
        return height