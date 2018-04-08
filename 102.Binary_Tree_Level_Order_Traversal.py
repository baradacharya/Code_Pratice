# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return None
        res = []
        queue = []
        cur_res = []
        if root.left:
            queue.append(root.left)
            cur_res.append(root.left.val)
        if root.right:
            queue.append(root.right)
            cur_res.append(root.right.val)
        res.append(cur_res)
        while 1:
            count = len(queue)
            if count == 0:
                break
            while count:
                cur_res = []
                temp = queue.pop(0)
                if temp.left:
                    queue.append(temp.left)
                    cur_res.append(temp.left.val)
                if temp.right:
                    queue.append(temp.right)
                    cur_res.append(temp.right.val)
                count -= 1
            res.append(cur_res)


