#https://leetcode.com/problems/next-permutation/solution/
"""
First, we observe that for any given sequence that is in descending order, no next larger permutation is possible.
Time complexity : O(n). In worst case, only two scans of the whole array are needed.

Space complexity : O(1). No extra space is used. In place replacements are done.
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= i and nums[j] <= nums[i]:
                j -= 1
            nums[i],nums[j] = nums[j],nums[i]
        self.reverse(nums,i+1)
        return nums
    def reverse(self,nums,l):
        r = len(nums) - 1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -=1
s = Solution()
# print s.nextPermutation([1,2,3])
# print s.nextPermutation([1,5,8,4,7,6,5,3,1])
print s.nextPermutation([9, 5, 4, 3, 1])