# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return root
        paths = []
        path = []
        self.BFS(root,paths,path)
        sum = 0
        for path in paths:
            num = 0
            for i in path:
                num = num *10 + i
            sum += num
        return sum

    def BFS(self,root,paths,path):
        if not root: return root
        if root.left == None and root.right == None:
            paths.append(path + [root.val])
            return
        self.BFS(root.left,paths, path + [root.val])
        self.BFS(root.right,paths, path + [root.val])
        return

    def create_Tree(self, ind, nums):
        """
        :param nums: list[int]
        :return: TreeNode
        """
        if ind >= len(nums): return None
        if nums[ind] == None:
            return None
        else:
            root = TreeNode(nums[ind])
        left_ind = 2 * ind + 1
        right_ind = 2 * ind + 2
        root.left = self.create_Tree(left_ind, nums)
        root.right = self.create_Tree(right_ind, nums)
        return root

    def pre_order_traversal(self, root):
        if not root: return None
        print (root.val)
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

s = Solution()
t = s.create_Tree(0, [0,1,3])
print s.sumNumbers(t)

