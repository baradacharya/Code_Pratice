# Definition for a binary tree node.
#queue/stack, hashmap
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #approach1 - DFS
    #1. Travese right side node first. So that on each level right side node will be first visited.
    #T:O(n) , S:O(n)
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        right_side_view = {} #store in a dict
        stack = [(root,0)]
        while stack:
            cur_node,depth = stack.pop()
            if depth not in right_side_view:
                right_side_view[depth] = cur_node.val
            if cur_node.left:  stack.append((cur_node.left, depth+1))
            if cur_node.right: stack.append((cur_node.right,depth+1))
        res = [right_side_view[val] for val in right_side_view]
        return res

    #2. BFS, travel in a levl order and put each level's end node
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        right_side_view = {} #store in a dict
        from collections import deque
        queue = deque([(root,0)])
        while queue:
            cur_node,depth = queue.popleft()
            right_side_view[depth] = cur_node.val #will store rightmost value of each level by overwriting
            if cur_node.left:  queue.append((cur_node.left, depth+1))
            if cur_node.right: queue.append((cur_node.right,depth+1))
        res = [right_side_view[val] for val in right_side_view]
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

    def pre_order_traversal(self, root):
        if not root: return None
        print (root.val)
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

s = Solution()
tree = s.create_Tree(0, [1,2,3,4,5])
s.pre_order_traversal(tree)
s.rightSideView(tree)
