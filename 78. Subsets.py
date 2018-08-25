"""
Subsets, Permutations, Combination Sum, Palindrome Partitioning
"""
class Solution(object):
    #1. using DFS
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # nums.sort()
        self.DFS(nums, 0, [], res)
        return res

    def DFS(self, nums, start, path, res):
        res.append(path)
        for i in range(start, len(nums)):
            self.DFS(nums, i + 1, path + [nums[i]], res)


s = Solution()
print s.subsets([1,2,3])
