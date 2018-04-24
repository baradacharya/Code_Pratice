"""
Given a collection of distinct integers, return all possible permutations.
"""
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
            if nums[i] in path: #don't send the same number.
                continue
            self.DFS(nums,path+[nums[i]],res)

s = Solution()
print s.permute([1,2,3])