#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: return True
        if not p : return False
        if not q: return False

        if p.val == q.val: return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True

        inverted_tree = self.invertedTree(root)
        if self.isSameTree(root,inverted_tree): return True
        else: return False

    def invertedTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None

        inverted_tree = TreeNode(root.val) #trick to create new tree
        inverted_tree.right = self.invertedTree(root.left)
        inverted_tree.left = self.invertedTree(root.right)
        return inverted_tree

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
tree = s.create_Tree(0,[1,2,2,3,4,4,3])
s.pre_order_traversal(tree)
print s.isSymmetric(tree)