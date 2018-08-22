# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        if not self.isLeaf(root):
            res.append(root.val)

        # 1. Add left boundary
        node = root.left
        while node:
            if not self.isLeaf(node):
                res.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right

        # 2.Add leaf nodes
        self.addLeaves(root, res)

        # 3. Add right boundary
        stack = []
        node = root.right
        while node:
            if not self.isLeaf(node):
                stack.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left

        while stack:
            res.append(stack.pop())
        return res

    def isLeaf(self, root):
        return not root.left and not root.right

    def addLeaves(self, root, res):
        if not root: return
        if self.isLeaf(root):
            res.append(root.val)
        else:
            self.addLeaves(root.left, res)
            self.addLeaves(root.right, res)

