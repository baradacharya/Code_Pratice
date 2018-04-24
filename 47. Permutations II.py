"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
sort for skipping sam value
when a number has same value with previous, we can use this number only if previous is used.
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        used = [False] * len(nums)
        self.DFS(nums, [], res,used)
        return res

    def DFS(self, nums, path, res, used):
        if len(path) == len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            if used[i]: continue
            #number has same value as previous and previous is used then we can use this number.
            if i > 0 and nums[i-1] == nums[i] and not used[i-1]:
                continue
            used[i] = True
            self.DFS(nums, path + [nums[i]], res, used)
            used[i] = False


s = Solution()
print s.permuteUnique([1,1,2])