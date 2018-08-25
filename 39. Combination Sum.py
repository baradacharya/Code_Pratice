"""
Subsets, Permutations, Combination Sum, Palindrome Partitioning
Backtrack
"""
#unique combinations
#The same repeated number may be chosen from candidates unlimited number of times.
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.DFS(candidates, target, 0, res, [])
        return res

    def DFS(self,candidates,target,start,res,path):
        print path
        if target < 0 :
            return
        if target == 0:
            res.append(path)
            return
        for i in range(start,len(candidates)):
            self.DFS(candidates, target - candidates[i],i,res,path+[candidates[i]])# not i+1 as we can reuse same i.

s = Solution()
print s.combinationSum([2,3,6,7],7)

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.DFS(nums,[],res)
        return res

    def DFS(self,nums,path,res):
        if len(path) == len(nums):
            res.append(path)
        for i in range(len(nums)):
            if nums[i] in path:  # don't send the same number.
                continue
            self.DFS(nums, path + [nums[i]], res)

# class Solution(object):
#     #1. using DFS
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         nums.sort()
#         self.DFS(sorted(nums),0,[],res)
#         return res
#     def DFS(self,nums,index,path,res):
#         res.append(path)
#         for i in range(index,len(nums)):
#             self.DFS(nums,i+1,path+[nums[i]],res)
#             #kind of backtracking by this step path+[nums[i]], will remove automatically