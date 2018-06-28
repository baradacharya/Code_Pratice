#the most frequently occurred element in the given BST.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#using extra space
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res =[]

        if not root : return res
        counter = {}

        def DFS(root):
            if not root: return
            counter[root.val] = counter.get(root.val, 0) + 1
            DFS(root.left)
            DFS(root.right)

        DFS(root)
        max_val = max(counter.values())
        for val in counter:
            if counter[val] == max_val:
                res.append(val)
        return res
