# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder,inorder[:ind])
            root.right = self.buildTree(preorder,inorder[ind+1:])
            return root
    def pre_order_traversal(self,root):
        if not root: return None
        print (root.val)
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

s = Solution()
t = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
s.pre_order_traversal(t)
