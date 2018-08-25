"""
T:O(n),S:O(n)
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = dict()
        for i,num in enumerate(nums):
            if num in num_dict:
                return (num_dict[num],i)
            else:
                num_dict[target - num] = i

s = Solution()
q = s.twoSum([2, 7, 11, 15],9)
print q
#T: O(n)
#if sorted less by using two pointer