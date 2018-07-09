# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if p.val < root.val:
            return self.inorderSuccessor(root.left, p) or root
        return self.inorderSuccessor(root.right, p)

    def inorderPredecessor(self, root, p):
        if not root:
            return None
        if p.val > root.val:
            return self.inorderSuccessor(root.right, p) or root
        return self.inorderSuccessor(root.left, p)


"""
1. If root is NULL
      then return
2. if key is found then
    a. If its left subtree is not null
        Then predecessor will be the right most 
        child of left subtree or left child itself.
    b. If its right subtree is not null
        The successor will be the left most child 
        of right subtree or right child itself.
    return
3. If key is smaller then root node
        set the successor as root
        search recursively into left subtree
    else
        set the predecessor as root
        search recursively into right subtree
"""
