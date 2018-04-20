# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root: return res
        stack = [(root,False)]
        while stack:
            cur_node,visited = stack.pop()
            if visited:
                res.append(cur_node.val)
            else:
                #postorder right,left,node
                stack.append((cur_node,True))
                if cur_node.right:
                    stack.append((cur_node.right,False))
                if cur_node.left:
                    stack.append((cur_node.left,False))
        return res
