"""
Approach #1 Sorting T:O(nlogn) S:O(1)
Approach #2 HashSet T:O(n) S:O(n)
3.  Bit Manipulation T:O(n) S:O(1)
4. use gauss n(n+1)/2
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = len(nums)
        for i,num in enumerate(nums):
            missing ^= i ^ num
        return missing