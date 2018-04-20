# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        #list is a mutable object so pass list
        self.dfs(root, sum, [], ans)
        return ans

    def dfs(self, root, sum, path, ans):
        if not root:
            return

        if root.left == None and root.right == None and sum == root.val:
            ans.append(path + [root.val])
            return

        self.dfs(root.left, sum - root.val, path + [root.val], ans) #imp tric path+[] which will back propogate
        self.dfs(root.right, sum - root.val, path + [root.val], ans)

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

    def pre_order_traversal(self,root):
        if not root: return None
        print (root.val)
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

s =Solution()

tree = s.create_Tree(0,[5,4,8,11,None,13,4,7,2,None,None,5,1])
s.pre_order_traversal(tree)
res = s.pathSum(tree,22)
print res