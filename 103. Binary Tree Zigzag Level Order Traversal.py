# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        queue = []
        res.append([root.val])
        queue.append(root)
        flag  = True
        while 1:
            count = len(queue)
            if count == 0:
                break
            cur_res = []
            while count:
                temp = queue.pop(0)
                count -= 1
                if temp.left:
                    queue.append(temp.left)
                    cur_res.append(temp.left.val)
                if temp.right:
                    queue.append(temp.right)
                    cur_res.append(temp.right.val)
            if len(cur_res):
                if flag:
                    cur_res.reverse()
                    res.append(cur_res)
                    flag = False
                else:
                    res.append(cur_res)
                    flag = True
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

    def pre_order_traversal(self, root):
        if not root: return None
        print (root.val)
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

s = Solution()
t =s.create_Tree(0,[3,9,20,None,None,15,7])
s.pre_order_traversal(t)
print s.zigzagLevelOrder(t)
