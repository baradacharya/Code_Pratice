# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if not root: return res
        self.DFS(root, res, [])
        res_str = []
        for list_ in res:
            s = ""
            s += str(list_[0])
            for i in range(1, len(list_)):
                s += "->"
                s += str(list_[i])
            res_str.append(s)
        return res_str

    def DFS(self, root, res, path):
        if not root.left and not root.right:
            res.append(path + [root.val])
            return
        if root.left: self.DFS(root.left, res, path + [root.val])
        if root.right: self.DFS(root.right, res, path + [root.val])
        return