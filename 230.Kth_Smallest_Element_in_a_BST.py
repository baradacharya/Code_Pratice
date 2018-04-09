# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.res = 0
        if not root: return 0
         #IMPORTANT To pass argument by call by reference a list need to be passed. because list is a mutable object
        self.inorder(root,k)
        return self.res

    def inorder(self,root,k):
        if not root: return
        self.inorder(root.left,k)
        self.count += 1
        if self.count == k :
            self.res = root.val
            return
        self.inorder(root.right,k)

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

s = Solution()
tree = s.create_Tree(0,[2,1])
s.pre_order_traversal(tree)
print s.kthSmallest(tree,1)