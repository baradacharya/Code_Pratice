# #376. Wiggle Subsequence
# import numpy as np
# def wiggleMaxLength(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     if len(nums)< 2:
#         return len(nums)
#     up =  [0] * len(nums)
#     down= [0] * len(nums)
#
#     for i in range(1,len(nums)):
#         for j in range(i):
#             if nums[i] > nums[j]:
#                 up[i] = max(up[i],1 + down[j])
#             elif nums[i] < nums[j]:
#                 down[i] =  max(1 + up[j],down[i])
#     return 1 + max(up[len(nums)-1],down[len(nums)-1])
# a = wiggleMaxLength([1,7,4,9,2,5])
# print(a)

# #95. Unique Binary Search Trees II
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution(object):
#     def generateTrees(self, n):
#         """
#         :type n: int
#         :rtype: List[TreeNode]
#         """
#         if n == 0:
#             return []
#         return self.dfs(1, n + 1)
#
#     def dfs(self, start, end):
#         if start == end:
#             return None
#         result = []
#         for i in xrange(start, end):
#             for l in self.dfs(start, i) or [None]:
#                 for r in self.dfs(i + 1, end) or [None]:
#                     node = TreeNode(i)
#                     node.left, node.right = l, r
#                     result.append(node)
#         return result
# s = Solution()
# t = s.generateTrees(3)
# print t
