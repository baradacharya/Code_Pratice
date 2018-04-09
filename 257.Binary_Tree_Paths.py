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
        if not root:
            return res
        self.bfspath(root, [], res)
        # return res
        res_str = []
        #for putting into format
        for list_ in res:
            s = ""
            s += str(list_[0])
            for i in range(1, len(list_)):
                s += "->"
                s += str(list_[i])
            res_str.append(s)
        return res_str

    def bfspath(self, root, path, res):
        if not root:
            return

        if (root.left == None and root.right == None):
            res.append(path + [root.val])

        self.bfspath(root.left, path + [root.val], res)
        self.bfspath(root.right, path + [root.val], res)