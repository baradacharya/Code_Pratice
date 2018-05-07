# Definition for a binary tree node.
import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    import sys
    maximum = - sys.maxint
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.maxSum_rec(root)
        return self.maximum

    def maxSum_rec(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        #we shoud n't add negative sum from the down.
        lsum = max(0,self.maxSum_rec(root.left))
        rsum = max(0,self.maxSum_rec(root.right))
        #lsum,rsum >= 0
        self.maximum = max(self.maximum,lsum + rsum+ root.val) #if the current root is the peak of path,update maximum variable
        return max(lsum,rsum)+ root.val #if current root is not the peak,root is along the path

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

s = Solution()
tree = s.create_Tree(0,[1,2,3])
print s.maxPathSum(tree)

