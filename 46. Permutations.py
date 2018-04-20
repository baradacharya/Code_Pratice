# class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         self.DFS(nums,[],res)
#         return res
#     def DFS(self,nums,path,res):
#         if len(path) == len(nums):
#             res.append(path)
#         for i in range(len(nums)):
#             self.DFS(nums,path+[nums[i]],res)
#
# s = Solution()
# #print s.permute([1,2,3])
# print s.permute([1,1,2])