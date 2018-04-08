class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def create_Tree(self, ind, nums):
        """
        :param nums: list[int]
        :return: TreeNode
        """
        if ind >= len(nums): return None
        root = TreeNode(nums[ind])
        left_ind = 2 * ind + 1
        right_ind = 2 * ind + 2
        root.left = self.create_Tree(left_ind, nums)
        root.right = self.create_Tree(right_ind, nums)
        return root

    def pre_order_traversal(self,root):
        if not root: return None
        print (root.val)
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

s = Solution()
tree = s.create_Tree(0,[1,2,2,3,4,4,3])
s.pre_order_traversal(tree)