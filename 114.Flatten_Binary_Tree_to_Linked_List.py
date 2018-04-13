# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return
        left = root.left
        right = root.right

        root.left = None
        self.flatten(left)
        self.flatten(right)

        root.right = left
        #find the end of left tree
        cur  = root
        while cur.right:
            cur =cur.right
        cur.right = right
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

s = Solution()
t = s.create_Tree(0,[1, 2, 5, 3, 4, None, 6])
s.flatten(t)
