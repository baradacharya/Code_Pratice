#BFS solution + Dictionary

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        import collections
        dict = collections.defaultdict(list)
        queue = [(root,0)] #node, x coordinate
        while queue:
            node,x = queue.pop(0)
            dict[x].append(node.val)
            if node.left:queue.append((node.left,x-1))
            if node.right: queue.append((node.right,x+1))
        res = []
        for key in sorted(dict):
            res.append(dict[key])
        return res

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

s = Solution()
tree = s.create_Tree(0,[3,9,20,None,None,15,7])
print s.verticalOrder(tree)
