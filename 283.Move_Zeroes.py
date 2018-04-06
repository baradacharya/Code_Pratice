"""
T:O(n), S:O(1)
"""
# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         last_nonzero  = 0
#         for i in range(len(nums)):
#             if nums[i] != 0 :
#                 nums[last_nonzero] = nums[i]
#                 last_nonzero += 1
#         for i in range(last_nonzero,len(nums)):
#             nums[i] = 0

#More optimal solution
def swap(s1, s2):
    return s2, s1

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last_nonzero  = 0
        for i in range(len(nums)):
            if nums[i] != 0 :
                # temp = nums[last_nonzero]
                nums[last_nonzero] = nums[i]
                nums[i] = 0
                last_nonzero += 1

s = Solution()
nums  = [0, 1, 0, 3, 12]
s.moveZeroes(nums)
print nums